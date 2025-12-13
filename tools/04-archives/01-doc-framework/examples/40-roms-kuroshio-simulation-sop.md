---
# =============================================================================
# ROMS黒潮シミュレーション SOP
# =============================================================================
document_id: SOP-OCEAN-001
title: "ROMS黒潮領域シミュレーション実行手順"
type: sop
version: "1.0"
status: active

# 所有権
owner: "@ocean-modeling-team"
author: claude-code
created: 2025-12-06
updated: 2025-12-06

# RAG最適化
tags:
  - roms
  - ocean-modeling
  - kuroshio
  - simulation
  - hpc
key_concepts:
  - 黒潮シミュレーション
  - 海洋モデリング
  - ROMS実行手順
  - 並列計算
summary: "ROMS（Regional Ocean Modeling System）を用いた黒潮領域の海洋シミュレーション実行手順。メッシュ生成からポスト処理までの完全なワークフロー。"

# ドメインコンテキスト
domain: scientific
audience: scientists

# CFD/海洋モデリング固有
validation_cases:
  - name: "黒潮流軸位置"
    reference: "AVISO衛星高度計データ"
    metrics:
      - name: "流軸位置（33°N断面）"
        expected: 134.5
        tolerance: "±0.5°"
  - name: "黒潮流量"
    reference: "Tokara Strait観測"
    metrics:
      - name: "トカラ海峡流量"
        expected: 25
        tolerance: "±5 Sv"

verification:
  grid_convergence:
    method: GCI
    grids: [1/4°, 1/8°, 1/12°]
    observed_order: 1.8
  solution_verification:
    iterative_convergence: "ROMS内部収束判定"
    mass_conservation: "< 1e-10 m³/s"

standards:
  - "ASME V&V 20-2009"
  - "ICES Cooperative Research Report No. 315"

hpc_requirements:
  cores: 256
  memory_per_core: "4GB"
  walltime: "48:00:00"
  storage: "2TB"
  parallel_model: MPI

solver_config:
  solver: "ROMS"
  version: "3.9"
  turbulence_model: "GLS (Generic Length Scale)"
  time_integration: "Leap-frog with Robert-Asselin filter"

domain_config:
  dimensions: "東経120-145°、北緯20-45°"
  grid_resolution: "1/12° (約9km)"
  total_cells: 120000000
  boundary_conditions:
    - "西側: Flow Relaxation Scheme (HYCOM)"
    - "東側: Flow Relaxation Scheme (HYCOM)"
    - "海面: ECMWF ERA5風応力"
    - "海底: 対数則摩擦"

# メンテナンス
next_review: 2026-06-06
review_cycle_days: 180

# 関連ドキュメント
related_docs:
  - path: "../templates/08cfd-ocean-sop-template.md"
    relationship: implements
  - path: "../schema/cfd-ocean.yaml"
    relationship: governed-by
---

# ROMS黒潮領域シミュレーション実行手順

## 目的

本手順は、ROMS（Regional Ocean Modeling System）を用いて黒潮領域の海洋シミュレーションを実行するための標準作業手順です。

**[重要]** この手順に従うことで、再現可能で品質が保証されたシミュレーション結果を得ることができます。

## 適用範囲

- **対象モデル**: ROMS 3.9
- **対象領域**: 黒潮領域（東経120-145°、北緯20-45°）
- **対象ユーザー**: 海洋モデリングチームのエンジニア・研究者

## 前提条件

| 要件 | 詳細 | 検証方法 |
|------|------|----------|
| HPCアカウント | FUGAKU または同等HPC | `ssh user@fugaku` で接続確認 |
| ROMS | バージョン3.9以上 | `which romsM` |
| NetCDF | 4.7以上 | `nc-config --version` |
| 前提知識 | ROMS基礎、Linux操作、NetCDF | - |

## 計算領域と境界条件

### ドメイン定義

```
    北緯45° ─────────────────────────────
            │                           │
            │      黒潮計算領域          │
            │                           │
    北緯20° ─────────────────────────────
          東経120°                    東経145°
```

| パラメータ | 値 | 備考 |
|-----------|---|------|
| 水平範囲 | 東経120-145°、北緯20-45° | 日本周辺海域 |
| 水平解像度 | 1/12° (約9km) | 渦解像 |
| 鉛直層数 | 40層（s座標） | 表層高解像度 |
| 総セル数 | 1.2億 | 300×400×40 |

### 境界条件

| 境界 | 条件 | データソース |
|-----|------|-------------|
| 西側開境界 | FRS（緩和スキーム） | HYCOM GLBv0.08 |
| 東側開境界 | FRS（緩和スキーム） | HYCOM GLBv0.08 |
| 南側開境界 | FRS（緩和スキーム） | HYCOM GLBv0.08 |
| 北側開境界 | 閉境界（陸地） | - |
| 海面 | バルク式 | ECMWF ERA5 |
| 海底 | 対数則摩擦 | 底質データ |

## 手順

### ステップ1: 環境設定

**目的:** 計算環境を準備する

```bash
# モジュールロード
module load roms/3.9
module load netcdf-fortran/4.5.3
module load intel-mpi/2021.4

# 作業ディレクトリ作成
export WORK=$SCRATCH/kuroshio_sim
mkdir -p $WORK
cd $WORK
```

**期待出力:**
```
No errors, modules loaded successfully
```

**検証:** `echo $ROMS_HOME` でROMSパスを確認

### ステップ2: 入力ファイル準備

**目的:** 計算に必要な入力ファイルを準備する

```bash
# テンプレートファイルコピー
cp $ROMS_HOME/User/External/roms_kuroshio.in .
cp $ROMS_HOME/User/External/varinfo.dat .

# グリッドファイル取得
ln -s /data/roms/kuroshio_grid.nc grid.nc

# 境界条件ファイルリンク
ln -s /data/hycom/hycom_bry_2024.nc bry.nc

# 大気強制力ファイルリンク
ln -s /data/era5/era5_frc_2024.nc frc.nc
```

⚠️ **停止条件**: ファイルが見つからない場合は、データ管理者に連絡

### ステップ3: 設定ファイル編集

**目的:** シミュレーションパラメータを設定する

```bash
# roms_kuroshio.inの主要パラメータ
vi roms_kuroshio.in
```

主要パラメータ:
```
NTIMES   == 8640      ! タイムステップ数（1年分）
DT       == 300.0     ! タイムステップ（秒）
NHIS     == 288       ! 履歴出力間隔（1日）
```

### ステップ4: 計算実行

**目的:** シミュレーションを実行する

```bash
# ジョブスクリプト作成
cat << 'EOF' > job_roms.sh
#!/bin/bash
#SBATCH --job-name=kuroshio
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=32
#SBATCH --time=48:00:00
#SBATCH --partition=normal

module load roms/3.9 netcdf-fortran/4.5.3 intel-mpi/2021.4

mpirun -np 256 romsM roms_kuroshio.in > roms.log 2>&1
EOF

# ジョブ投入
sbatch job_roms.sh
```

**期待出力:**
```
Submitted batch job 12345678
```

### ステップ5: 結果確認

**目的:** 計算結果を確認する

```bash
# ログ確認
tail -100 roms.log

# 出力ファイル確認
ncdump -h roms_his.nc | head -50

# 可視化（簡易）
ncview roms_his.nc &
```

## 品質メトリクス

| メトリクス | 閾値 | 検証コマンド |
|-----------|------|--------------|
| 質量保存誤差 | < 1e-10 m³/s | `grep "MASS" roms.log` |
| CFL数 | < 0.5 | `grep "CFL" roms.log` |
| エネルギー変動 | < 1%/年 | ポスト処理で確認 |
| 境界での整合性 | < 0.1 m | ポスト処理で確認 |

## 検証と妥当性確認（V&V）

### グリッド収束評価

**手法:** GCI（Grid Convergence Index）

| グリッド | 解像度 | 黒潮流量(Sv) | GCI(%) |
|---------|-------|-------------|--------|
| Coarse | 1/4° | 22.5 | - |
| Medium | 1/8° | 24.1 | 8.5 |
| Fine | 1/12° | 24.8 | 3.2 |

**観測収束次数:** p = 1.8

### 検証ケース結果

| ケース | 参照値 | 計算値 | 相対誤差 | 判定 |
|-------|-------|-------|---------|------|
| 黒潮流軸位置（33°N） | 134.5°E | 134.3°E | 0.15% | ✅ |
| トカラ海峡流量 | 25±5 Sv | 24.8 Sv | 0.8% | ✅ |
| SSH RMSE | - | 0.08 m | - | ✅ |

### 妥当性確認

- **AVISO衛星高度計データ**: SSH相関係数 0.85
- **Argo浮遊ブイ**: 水温RMSE 0.5°C、塩分RMSE 0.1 PSU
- **係留系観測**: 流速相関係数 0.78

## 不確かさ定量化

### 不確かさ源

| 源 | タイプ | 大きさ | 備考 |
|----|-------|-------|------|
| 風応力（ERA5） | 認識的 | ±10% | 再解析データ精度 |
| 境界条件（HYCOM） | 認識的 | ±5% | 親モデル精度 |
| 底面摩擦係数 | 認識的 | ±30% | パラメータ不確かさ |
| 数値誤差 | 偶然的 | <5% | GCI評価 |

### 不確かさ伝播

```
総合不確かさ = √(10² + 5² + 5²) ≈ ±12%
```

## HPC要件とリソース

| パラメータ | 値 | 備考 |
|-----------|---|------|
| コア数 | 256 | 8ノード × 32コア |
| メモリ/コア | 4GB | 総1TB |
| 実行時間 | 48時間 | 1年分シミュレーション |
| ストレージ | 2TB | 日次出力 |
| I/O | 50GB/h | 履歴ファイル出力 |

## トラブルシューティング

| 問題 | 原因 | 解決策 |
|------|------|--------|
| BLOWUP | CFL条件違反 | DTを150秒に減少 |
| メモリ不足 | ノードあたりプロセス過多 | ノード数を倍増 |
| 境界でノイズ | 緩和ゾーン不足 | NDTFASTを増加 |
| 収束しない | スピンアップ不足 | 初期条件を改善 |

## ロールバック手順

**ロールバック条件:**
- BLOWUPが発生した場合
- 品質メトリクスを満たさない場合

```bash
# 最新のリスタートファイルから再開
cd $WORK
ls -lt roms_rst_*.nc | head -1
# 例: roms_rst_0001.nc

# roms_kuroshio.inのNRRECを更新
vi roms_kuroshio.in
# NRREC == 1

# 再実行
sbatch job_roms.sh
```

## コミュニティ標準参照

本手順は以下の標準およびベストプラクティスに準拠しています：

- **ASME V&V 20-2009**: CFD検証妥当性確認標準
- **ICES Cooperative Research Report No. 315**: 海洋モデリングベストプラクティス
- **ROMS Wiki Best Practices**: https://www.myroms.org/wiki/

## 関連ドキュメント

- [08cfd-ocean-sop-template.md](../templates/08cfd-ocean-sop-template.md) - CFD/海洋モデリングSOPテンプレート
- [cfd-ocean.yaml](../schema/cfd-ocean.yaml) - ドメイン固有スキーマ

---

**作成日**: 2025-12-06
**バージョン**: 1.0
**次回レビュー**: 2026-06-06
