#!/usr/bin/env python3
"""
模型下載腳本
自動下載所需的AI模型文件
"""

import os
import sys
import logging
from pathlib import Path
from huggingface_hub import snapshot_download, login
import torch

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def download_models():
    """下載所需的AI模型"""
    
    models_to_download = [
        {
            "name": "FLAN-T5-Large (文案生成)",
            "repo_id": "google/flan-t5-large",
            "local_dir": "checkpoints/flan-t5-large"
        },
        {
            "name": "SDXL Base (圖像生成)",
            "repo_id": "stabilityai/stable-diffusion-xl-base-1.0", 
            "local_dir": "checkpoints/sdxl-base-1.0"
        },
        {
            "name": "SDXL Refiner (圖像增強)",
            "repo_id": "stabilityai/stable-diffusion-xl-refiner-1.0",
            "local_dir": "checkpoints/sdxl-refiner-1.0"
        },
        {
            "name": "SVD (影片生成)",
            "repo_id": "stabilityai/stable-video-diffusion-img2vid-xt",
            "local_dir": "checkpoints/svd-img2vid-xt"
        }
    ]
    
    # 檢查CUDA
    if torch.cuda.is_available():
        logger.info(f"✅ 檢測到GPU: {torch.cuda.get_device_name(0)}")
        logger.info(f"   VRAM: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f}GB")
    else:
        logger.warning("⚠️ 未檢測到CUDA GPU，將使用CPU模式")
    
    # 創建checkpoints目錄
    checkpoints_dir = Path("checkpoints")
    checkpoints_dir.mkdir(exist_ok=True)
    
    # 嘗試登錄Hugging Face (如果有token)
    hf_token = os.getenv("HUGGINGFACE_TOKEN")
    if hf_token:
        try:
            login(token=hf_token)
            logger.info("✅ Hugging Face 登錄成功")
        except Exception as e:
            logger.warning(f"Hugging Face 登錄失敗: {e}")
    
    # 下載模型
    for model_info in models_to_download:
        try:
            logger.info(f"📥 開始下載: {model_info['name']}")
            
            local_path = Path(model_info["local_dir"])
            
            # 檢查是否已存在
            if local_path.exists() and any(local_path.iterdir()):
                logger.info(f"✅ 模型已存在，跳過: {model_info['name']}")
                continue
            
            # 下載模型
            snapshot_download(
                repo_id=model_info["repo_id"],
                local_dir=model_info["local_dir"],
                local_dir_use_symlinks=False,
                resume_download=True
            )
            
            logger.info(f"✅ 下載完成: {model_info['name']}")
            
        except Exception as e:
            logger.error(f"❌ 下載失敗 {model_info['name']}: {e}")
            
            # 對於某些模型，提供替代方案
            if "sdxl" in model_info["repo_id"]:
                logger.info("💡 提示: SDXL模型需要約13GB空間，確保有足夠的磁碟空間")
            elif "svd" in model_info["repo_id"]:
                logger.info("💡 提示: SVD模型需要約9GB空間和16GB+ VRAM")
    
    logger.info("🎉 模型下載流程完成！")
    
    # 檢查下載結果
    logger.info("\n📊 模型狀態檢查:")
    for model_info in models_to_download:
        local_path = Path(model_info["local_dir"])
        if local_path.exists() and any(local_path.iterdir()):
            size_mb = sum(f.stat().st_size for f in local_path.rglob('*') if f.is_file()) / 1024**2
            logger.info(f"✅ {model_info['name']}: {size_mb:.1f}MB")
        else:
            logger.warning(f"❌ {model_info['name']}: 未找到")

if __name__ == "__main__":
    download_models()