#!/usr/bin/env python3
"""
完整修正版AI營銷系統
專為 http://140.119.124.214 公網部署
完整功能：文字生成 + 圖片設計 + 影片製作
解決所有網絡和編碼問題
"""

import gradio as gr
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from datetime import datetime
import time
import threading
import socket
import sys

# 確保輸出目錄存在
output_dirs = Path("outputs")
for subdir in ["text", "images", "videos"]:
    (output_dirs / subdir).mkdir(parents=True, exist_ok=True)

class CompleteAIMarketingSystem:
    def __init__(self):
        self.running = True
        self.version = "1.0.0 Final Fixed"
        self.public_ip = "140.119.124.214"  # 更新為實際IP
        print("🚀 完整修正版AI營銷系統初始化")
        self.check_system_status()
    
    def check_system_status(self):
        """檢查系統狀態"""
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            print(f"📊 系統狀態:")
            print(f"   版本: {self.version}")
            print(f"   主機: {hostname}")
            print(f"   本地IP: {local_ip}")
            print(f"   公網IP: {self.public_ip}")
            print(f"   狀態: ✅ 就緒")
        except Exception as e:
            print(f"⚠️ 系統檢查警告: {e}")
    
    def generate_content(self, product, style, audience, features, tone):
        """專業文案生成"""
        try:
            templates = {
                "專業商務": {
                    "formal": f"""# {product} - 企業級專業解決方案

## 核心優勢
{features}

## 目標客群
專為{audience}設計的專業服務

## 品質保證
✓ 國際標準認證
✓ 24/7專業支援
✓ 投資回報保證
✓ 專業團隊服務

**專業選擇，成功保證**

---
聯繫方式：professional@company.com
立即諮詢專業解決方案""",

                    "persuasive": f"""🎯 {product} - 領導者的明智選擇

💎 **獨家優勢**
{features}

🏆 **專為{audience}量身打造**

🔥 **限時優惠方案**
• 新客戶享8折優惠
• 免費試用60天
• 一對一專家諮詢
• 成功案例分享

📞 **立即行動**
機會有限，搶佔市場先機！

**成功企業的共同選擇**"""
                },
                
                "創新科技": {
                    "formal": f"""# {product} - 科技創新驅動

## 技術突破
{features}

## 應用領域
為{audience}提供智能化解決方案

## 技術優勢
• AI智能演算法
• 雲端數據整合
• 企業級安全保障
• 即時分析處理

**科技賦能，引領未來**

---
技術支援：tech@company.com
體驗未來科技解決方案""",

                    "persuasive": f"""🚀 {product} - 科技改變一切

⚡ **革命性突破**
{features}

🤖 **{audience}的智慧之選**

💫 **搶先體驗**
• 早鳥特價5折起
• 終身免費升級
• 專家培訓課程
• VIP技術支援

🎁 **限量測試名額**
成為科技先驅者！

**未來已來，你準備好了嗎？**"""
                },
                
                "溫馨生活": {
                    "formal": f"""{product} - 品質生活的選擇

為每個家庭帶來溫暖美好
{features}

用心呵護{audience}的每一天

我們承諾：
• 安全環保材料
• 人性化設計
• 嚴格品質管控
• 貼心售後服務

讓生活更有溫度
讓家更有愛的味道

---
客服熱線：service@company.com
讓愛住進每個角落""",

                    "persuasive": f"""❤️ {product} - 家的溫馨時光

🏠 **為家人帶來**
{features}

👨‍👩‍👧‍👦 **{audience}的貼心選擇**

💕 **溫馨優惠**
• 家庭套裝7折優惠
• 滿意保證退換
• 會員積分回饋
• 生日專屬優惠

🎁 **愛的禮物**
給最愛的人最好的呵護

**讓愛充滿每個角落**"""
                }
            }
            
            content = templates.get(style, templates["專業商務"]).get(tone, templates["專業商務"]["formal"])
            
            # 儲存檔案
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"content_{timestamp}.txt"
            filepath = output_dirs / "text" / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
            return content, f"✅ 文案生成成功\n📄 檔案：{filename}\n🎨 風格：{style}\n📝 語調：{tone}\n📊 字數：{len(content)}"
            
        except Exception as e:
            return f"生成過程中發生錯誤：{str(e)}", f"❌ 生成失敗：{str(e)}"
    
    def generate_image(self, prompt, style, size, quality):
        """專業圖片生成"""
        try:
            # 解析尺寸
            if "(" in size:
                size = size.split("(")[0].strip()
            width, height = map(int, size.split('x'))
            
            # 配色方案
            color_schemes = {
                "商業攝影": {"bg": "#f8f9fa", "primary": "#2c3e50", "secondary": "#3498db", "accent": "#e74c3c"},
                "創意設計": {"bg": "#ffffff", "primary": "#8e44ad", "secondary": "#e67e22", "accent": "#f39c12"},
                "品牌形象": {"bg": "#ecf0f1", "primary": "#34495e", "secondary": "#1abc9c", "accent": "#e74c3c"},
                "社交媒體": {"bg": "#fafafa", "primary": "#e91e63", "secondary": "#9c27b0", "accent": "#ff5722"},
                "印刷媒體": {"bg": "#f5f5f5", "primary": "#607d8b", "secondary": "#795548", "accent": "#ff9800"}
            }
            
            colors = color_schemes.get(style, color_schemes["商業攝影"])
            
            # 創建圖片
            img = Image.new('RGB', (width, height), colors["bg"])
            draw = ImageDraw.Draw(img)
            
            # 漸變背景
            for y in range(height):
                ratio = y / height
                bg_rgb = tuple(int(colors["bg"][i:i+2], 16) for i in (1, 3, 5))
                primary_rgb = tuple(int(colors["primary"][i:i+2], 16) for i in (1, 3, 5))
                
                r = int(bg_rgb[0] * (1-ratio*0.2) + primary_rgb[0] * ratio*0.1)
                g = int(bg_rgb[1] * (1-ratio*0.2) + primary_rgb[1] * ratio*0.1)  
                b = int(bg_rgb[2] * (1-ratio*0.2) + primary_rgb[2] * ratio*0.1)
                
                draw.line([(0, y), (width, y)], fill=(r, g, b))
            
            # 裝飾元素
            center_x, center_y = width // 2, height // 2
            
            # 幾何裝飾
            for i in range(3):
                radius = 30 + i * 20
                x = center_x + (i-1) * 60
                y = center_y + (i-1) * 30
                
                secondary_rgb = tuple(int(colors["secondary"][i:i+2], 16) for i in (1, 3, 5))
                draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                           outline=secondary_rgb, width=2)
            
            # 文字內容
            font = ImageFont.load_default()
            
            # 主標題
            title = "AI Marketing Pro"
            title_bbox = draw.textbbox((0, 0), title, font=font)
            title_w = title_bbox[2] - title_bbox[0]
            primary_rgb = tuple(int(colors["primary"][i:i+2], 16) for i in (1, 3, 5))
            draw.text((center_x - title_w//2, center_y - 50), title, fill=primary_rgb, font=font)
            
            # 副標題
            subtitle = style
            sub_bbox = draw.textbbox((0, 0), subtitle, font=font)
            sub_w = sub_bbox[2] - sub_bbox[0]
            secondary_rgb = tuple(int(colors["secondary"][i:i+2], 16) for i in (1, 3, 5))
            draw.text((center_x - sub_w//2, center_y - 15), subtitle, fill=secondary_rgb, font=font)
            
            # 描述文字
            desc = prompt[:35] + "..." if len(prompt) > 35 else prompt
            desc_text = f'"{desc}"'
            desc_bbox = draw.textbbox((0, 0), desc_text, font=font)
            desc_w = desc_bbox[2] - desc_bbox[0]
            draw.text((center_x - desc_w//2, center_y + 20), desc_text, fill=primary_rgb, font=font)
            
            # 專業邊框
            draw.rectangle([0, 0, width-1, height-1], outline=primary_rgb, width=2)
            accent_rgb = tuple(int(colors["accent"][i:i+2], 16) for i in (1, 3, 5))
            draw.rectangle([3, 3, width-4, height-4], outline=accent_rgb, width=1)
            
            # 儲存
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"image_{timestamp}.png"
            filepath = output_dirs / "images" / filename
            img.save(filepath, quality=quality, optimize=True)
            
            return str(filepath), f"✅ 圖片生成成功\n📄 檔案：{filename}\n📐 尺寸：{size}\n🎨 風格：{style}\n⭐ 品質：{quality}%"
            
        except Exception as e:
            return None, f"❌ 圖片生成失敗：{str(e)}"
    
    def generate_video(self, title, style, duration, resolution):
        """專業影片生成"""
        try:
            # 解析解析度
            if "(" in resolution:
                resolution = resolution.split("(")[0].strip()
            width, height = map(int, resolution.split('x'))
            fps = 25
            frames = int(duration * fps)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"video_{timestamp}.mp4"
            filepath = output_dirs / "videos" / filename
            
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(str(filepath), fourcc, fps, (width, height))
            
            print(f"🎬 製作影片：{title} - {style}")
            
            for i in range(frames):
                progress = i / frames
                
                if style == "產品展示":
                    frame = self._create_product_frame(title, progress, width, height)
                elif style == "品牌動畫":
                    frame = self._create_brand_frame(title, progress, width, height)
                elif style == "促銷廣告":
                    frame = self._create_promo_frame(title, progress, width, height, i)
                else:
                    frame = self._create_corporate_frame(title, progress, width, height)
                
                out.write(frame)
            
            out.release()
            
            return str(filepath), f"✅ 影片製作完成\n📄 檔案：{filename}\n⏱️ 時長：{duration}秒\n📺 解析度：{resolution}\n🎨 風格：{style}"
            
        except Exception as e:
            return None, f"❌ 影片製作失敗：{str(e)}"
    
    def _create_product_frame(self, title, progress, w, h):
        """產品展示幀"""
        img = np.zeros((h, w, 3), dtype=np.uint8)
        
        # 漸變背景
        for y in range(h):
            intensity = int(240 - (y/h)*30 + np.sin(progress*np.pi*2)*10)
            img[y, :] = [intensity-15, intensity-8, intensity]
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # 主標題動畫
        scale = 1.2 + np.sin(progress*np.pi*3)*0.1
        title_size = cv2.getTextSize(title, font, scale, 2)[0]
        title_x = (w - title_size[0]) // 2
        title_y = h // 3
        
        if progress > 0.1:
            cv2.putText(img, title, (title_x, title_y), font, scale, (60, 60, 180), 2)
        
        # 特色展示
        if progress > 0.3:
            features = ["Professional", "High Quality", "Reliable", "Innovative"]
            for j, feature in enumerate(features):
                if progress > 0.3 + j*0.1:
                    feat_y = title_y + 60 + j*30
                    feat_size = cv2.getTextSize(feature, font, 0.6, 2)[0]
                    feat_x = (w - feat_size[0]) // 2
                    
                    cv2.rectangle(img, (feat_x-5, feat_y-18), 
                                (feat_x+feat_size[0]+5, feat_y+5), (80, 120, 160), -1)
                    cv2.putText(img, feature, (feat_x, feat_y), font, 0.6, (255, 255, 255), 2)
        
        # 邊框
        cv2.rectangle(img, (10, 10), (w-10, h-10), (100, 100, 180), 2)
        return img
    
    def _create_brand_frame(self, title, progress, w, h):
        """品牌動畫幀"""
        img = np.zeros((h, w, 3), dtype=np.uint8)
        center_x, center_y = w // 2, h // 2
        
        # 動態背景
        for y in range(h):
            wave = np.sin((y/h + progress)*np.pi*3) * 20
            intensity = int(80 + wave)
            img[y, :] = [intensity//3, intensity//2, intensity]
        
        # 同心圓動畫
        for ring in range(3):
            radius = int(40 + ring*15 + progress*50)
            if radius < w//2:
                thickness = 2
                intensity = 200 - ring*20
                color = (intensity//4, intensity//2, intensity)
                cv2.circle(img, (center_x, center_y), radius, color, thickness)
        
        # 品牌標題
        font = cv2.FONT_HERSHEY_SIMPLEX
        scale = 1.0 + np.sin(progress*np.pi*4)*0.08
        
        title_size = cv2.getTextSize(title, font, scale, 2)[0]
        title_x = (w - title_size[0]) // 2
        title_y = center_y + 80
        
        cv2.putText(img, title, (title_x, title_y), font, scale, (220, 180, 240), 2)
        
        if progress > 0.4:
            tagline = "Professional Excellence"
            tag_size = cv2.getTextSize(tagline, font, 0.5, 2)[0]
            tag_x = (w - tag_size[0]) // 2
            cv2.putText(img, tagline, (tag_x, title_y + 30), font, 0.5, (180, 180, 220), 2)
        
        return img
    
    def _create_promo_frame(self, title, progress, w, h, frame_i):
        """促銷廣告幀"""
        flash = (frame_i // 6) % 2
        base_intensity = 90 if flash else 70
        
        img = np.full((h, w, 3), base_intensity, dtype=np.uint8)
        
        # 動態條紋
        for stripe in range(0, h, 30):
            stripe_intensity = base_intensity + (20 if flash else 10)
            cv2.rectangle(img, (0, stripe), (w, stripe + 15),
                        (stripe_intensity//3, stripe_intensity//2, stripe_intensity), -1)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # 主標題閃爍
        scale = 1.4 + (0.1 if flash else 0)
        title_size = cv2.getTextSize(title, font, scale, 3)[0]
        title_x = (w - title_size[0]) // 2
        title_y = h // 2 - 40
        
        color = (255, 255, 120) if flash else (220, 220, 255)
        cv2.putText(img, title, (title_x, title_y), font, scale, color, 3)
        
        # 促銷標語
        if progress > 0.2:
            promos = ["SPECIAL OFFER!", "LIMITED TIME!", "ACT NOW!"]
            promo = promos[frame_i // 10 % len(promos)]
            
            promo_size = cv2.getTextSize(promo, font, 0.8, 2)[0]
            promo_x = (w - promo_size[0]) // 2
            promo_y = title_y + 60
            
            if flash:
                cv2.rectangle(img, (promo_x-10, promo_y-25), 
                            (promo_x+promo_size[0]+10, promo_y+5), (255, 60, 60), -1)
                cv2.putText(img, promo, (promo_x, promo_y), font, 0.8, (255, 255, 255), 2)
            else:
                cv2.putText(img, promo, (promo_x, promo_y), font, 0.8, (255, 120, 120), 2)
        
        return img
    
    def _create_corporate_frame(self, title, progress, w, h):
        """企業形象幀"""
        img = np.zeros((h, w, 3), dtype=np.uint8)
        
        # 企業背景
        for y in range(h):
            intensity = int(220 - (y/h)*40)
            img[y, :] = [intensity-25, intensity-12, intensity]
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        center_x, center_y = w // 2, h // 2
        
        # 企業標題
        scale = 1.1
        title_size = cv2.getTextSize(title, font, scale, 2)[0]
        title_x = (w - title_size[0]) // 2
        
        cv2.putText(img, title, (title_x, center_y), font, scale, (80, 100, 180), 2)
        
        # 企業價值
        values = ["Quality", "Innovation", "Trust", "Excellence"]
        for j, value in enumerate(values):
            if progress > j * 0.15:
                angle = j * 90 + progress * 200
                radius = 70
                x = int(center_x + radius * np.cos(np.radians(angle)))
                y = int(center_y + radius * np.sin(np.radians(angle)))
                
                val_size = cv2.getTextSize(value, font, 0.4, 1)[0]
                val_x = x - val_size[0]//2
                val_y = y + val_size[1]//2
                
                cv2.putText(img, value, (val_x, val_y), font, 0.4, (120, 140, 200), 1)
        
        cv2.rectangle(img, (10, 10), (w-10, h-10), (90, 110, 170), 2)
        return img

def create_complete_interface():
    """創建完整界面"""
    
    ai_system = CompleteAIMarketingSystem()
    
    # 專業科技感UI設計 - 基於UI專家建議優化
    css = """
    /* 主容器 - 科技深藍 #0A192F */
    .gradio-container {
        font-family: 'Noto Sans TC', 'Microsoft JhengHei', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        max-width: 1200px;
        margin: 0 auto;
        background: #0A192F;
        min-height: 100vh;
        color: #E0E7FF;
        line-height: 1.5;
    }
    
    /* 簡潔的標題區域 */
    .header {
        background: #0A192F;
        padding: 2rem;
        text-align: center;
        margin: 0;
        border-bottom: 1px solid rgba(224, 231, 255, 0.1);
    }
    
    /* 功能區塊 */
    .section {
        background: #0A192F;
        padding: 1.5rem 2rem;
        margin: 0;
        border: none;
        border-bottom: 1px solid rgba(224, 231, 255, 0.05);
    }
    /* 專業色彩系統 - 按UI專家建議 */
    
    /* 狀態指示器 - 霓虹綠 #39FF14 */
    .status-online {
        color: #39FF14 !important;
        font-weight: 600;
        font-size: 1.0rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        text-shadow: 0 0 8px rgba(57, 255, 20, 0.3);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    /* 主標題 - 柔和白色 #E0E7FF */
    .main-title {
        color: #E0E7FF !important;
        font-weight: 300;
        font-size: 2.2rem;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }
    
    /* 功能名稱 - 天藍色 #00BFFF */
    .feature-text {
        color: #00BFFF !important;
        font-weight: 500;
        font-size: 1.0rem;
    }
    
    /* 使用指南標題 - 柔和紫 #A478E6 */
    .guide-title {
        color: #A478E6 !important;
        font-weight: 600;
        font-size: 1.3rem;
        margin-bottom: 1rem;
    }
    
    /* 主要文字 - 柔和白色 */
    .primary-text {
        color: #E0E7FF !important;
        font-weight: 400;
    }
    
    /* 副標題和提示 - 藍灰色 #8F99B3 */
    .subtitle {
        color: #8F99B3 !important;
        font-weight: 400;
        font-size: 1.0rem;
    }
    /* 專業UI組件 - 科技感微互動設計 */
    
    /* 全局統一背景 */
    .gradio-container *, .gr-form, .gr-box, .gr-panel, .gr-block {
        background: #0A192F !important;
        border: none !important;
    }
    
    /* 輕盈Tab設計 */
    .gradio-tabs {
        background: #0A192F !important;
        border-bottom: 1px solid rgba(224, 231, 255, 0.08) !important;
    }
    .gradio-tabs .tab-nav button {
        background: transparent !important;
        color: #8F99B3 !important;
        border: none !important;
        border-bottom: 2px solid transparent !important;
        border-radius: 0 !important;
        font-weight: 500 !important;
        font-size: 0.9rem !important;
        padding: 1rem 1.5rem !important;
        margin: 0 !important;
        transition: all 0.3s ease !important;
    }
    .gradio-tabs .tab-nav button.selected {
        background: transparent !important;
        color: #E0E7FF !important;
        border-bottom: 2px solid #00BFFF !important;
    }
    .gradio-tabs .tab-nav button:hover {
        color: #E0E7FF !important;
        background: rgba(0, 191, 255, 0.05) !important;
        box-shadow: 0 2px 8px rgba(0, 191, 255, 0.1) !important;
    }
    
    /* 表單標籤 - 柔和白色 */
    label, .gr-form label {
        color: #E0E7FF !important;
        font-weight: 500 !important;
        font-size: 0.85rem !important;
        margin-bottom: 0.4rem !important;
        line-height: 1.5 !important;
    }
    
    /* 輸入框 - 層次分明設計 #1E2C48 */
    input, textarea, select {
        background: #1E2C48 !important;
        color: #E0E7FF !important;
        border: 1px solid rgba(224, 231, 255, 0.15) !important;
        border-radius: 4px !important;
        padding: 0.7rem !important;
        font-size: 0.85rem !important;
        transition: all 0.3s ease !important;
    }
    input:focus, textarea:focus, select:focus {
        border-color: #00BFFF !important;
        box-shadow: 0 0 0 2px rgba(0, 191, 255, 0.2) !important;
        outline: none !important;
        background: #243654 !important;
    }
    
    /* 按鈕 - 天藍色科技感 #00BFFF */
    button {
        background: #00BFFF !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        font-size: 0.8rem !important;
        padding: 0.7rem 1.3rem !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 0.8px !important;
        box-shadow: 0 2px 8px rgba(0, 191, 255, 0.2) !important;
    }
    button:hover {
        background: #0099CC !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 16px rgba(0, 191, 255, 0.35) !important;
    }
    button:active {
        transform: translateY(-1px) !important;
        box-shadow: 0 3px 12px rgba(0, 191, 255, 0.4) !important;
    }
    
    /* 輸出區域 - 內容與容器分明 */
    .gr-textbox, .gr-image, .gr-video, .gr-file {
        background: #1E2C48 !important;
        border: 1px solid rgba(224, 231, 255, 0.12) !important;
        border-radius: 6px !important;
        color: #E0E7FF !important;
    }
    
    /* 滑桿現代設計 */
    .gr-slider {
        background: transparent !important;
    }
    .gr-slider input[type="range"] {
        background: #1E2C48 !important;
        border-radius: 10px !important;
        border: 1px solid rgba(224, 231, 255, 0.1) !important;
    }
    
    /* 專業表格設計 */
    table {
        border-collapse: separate !important;
        border-spacing: 0 !important;
        border-radius: 6px !important;
        overflow: hidden !important;
        border: 1px solid rgba(224, 231, 255, 0.15) !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
    }
    td {
        background: #1E2C48 !important;
        color: #E0E7FF !important;
        padding: 0.9rem 1.2rem !important;
        border-bottom: 1px solid rgba(224, 231, 255, 0.08) !important;
        font-size: 0.85rem !important;
        line-height: 1.4 !important;
    }
    td:first-child {
        font-weight: 600 !important;
        width: 28% !important;
        color: #8F99B3 !important;
    }
    
    /* 微互動效果 */
    .processing {
        animation: glow 1.5s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from {
            box-shadow: 0 0 5px #00BFFF, 0 0 10px #00BFFF, 0 0 15px #00BFFF;
        }
        to {
            box-shadow: 0 0 10px #00BFFF, 0 0 20px #00BFFF, 0 0 30px #00BFFF;
        }
    }
    """
    
    with gr.Blocks(title="AI Marketing System - Complete Fixed", theme=gr.themes.Soft(), css=css) as demo:
        
        gr.HTML(f"""
        <div class="header">
            <h1 class="main-title">AI營銷系統</h1>
            <h2 class="subtitle">完整專業營銷內容生成平台</h2>
            
            <div style="margin: 1.5rem 0; text-align: center;">
                <span class="status-online">ONLINE</span>
                <span class="subtitle" style="margin-left: 1.5rem;">版本: {ai_system.version} | 狀態: 生產就緒</span>
            </div>
        </div>
        """)
        
        with gr.Tabs():
            # 文案生成
            with gr.Tab("專業文案生成"):
                gr.HTML('<div class="section"><h3 class="guide-title">AI驅動的專業營銷文案創作</h3></div>')
                
                with gr.Row():
                    with gr.Column():
                        product_name = gr.Textbox(
                            label="產品/服務名稱",
                            value="AI營銷解決方案",
                            placeholder="輸入您的產品或服務名稱"
                        )
                        content_style = gr.Dropdown(
                            label="營銷風格",
                            choices=["專業商務", "創新科技", "溫馨生活"],
                            value="專業商務"
                        )
                        target_audience = gr.Textbox(
                            label="目標客群",
                            value="企業決策者和專業人士",
                            placeholder="描述您的目標客戶群體"
                        )
                        key_features = gr.Textbox(
                            label="核心特色與優勢",
                            lines=4,
                            value="• 高效能與可靠性保證\n• 24/7專業技術支援\n• 經驗證的投資回報率\n• 行業領先創新技術",
                            placeholder="列出主要特色、優勢和賣點"
                        )
                        tone_style = gr.Radio(
                            label="內容語調",
                            choices=[("專業正式", "formal"), ("營銷說服", "persuasive")],
                            value="formal"
                        )
                        generate_content_btn = gr.Button("生成專業文案", variant="primary", size="lg")
                    
                    with gr.Column():
                        content_output = gr.Textbox(
                            label="生成的營銷文案",
                            lines=18,
                            show_copy_button=True,
                            placeholder="您的專業營銷文案將在這裡顯示..."
                        )
                        content_info = gr.Textbox(label="生成狀態資訊", lines=4)
            
            # 圖片設計
            with gr.Tab("專業圖片設計"):
                gr.HTML('<div class="section"><h3 class="guide-title">AI驅動的專業營銷圖片創建</h3></div>')
                
                with gr.Row():
                    with gr.Column():
                        img_prompt = gr.Textbox(
                            label="圖片描述",
                            lines=3,
                            value="專業營銷設計，現代簡潔風格",
                            placeholder="描述您想要創建的營銷圖片"
                        )
                        img_style = gr.Dropdown(
                            label="設計風格",
                            choices=["商業攝影", "創意設計", "品牌形象", "社交媒體", "印刷媒體"],
                            value="商業攝影"
                        )
                        img_size = gr.Dropdown(
                            label="圖片尺寸",
                            choices=["1920x1080 (HD橫向)", "1080x1080 (方形)", "1080x1920 (直向)", "1200x630 (橫幅)"],
                            value="1920x1080 (HD橫向)"
                        )
                        img_quality = gr.Slider(
                            label="圖片品質",
                            minimum=75,
                            maximum=100,
                            value=90,
                            step=5
                        )
                        generate_image_btn = gr.Button("創建專業圖片", variant="primary", size="lg")
                    
                    with gr.Column():
                        image_output = gr.Image(label="生成的營銷圖片", height=400)
                        image_info = gr.Textbox(label="創建狀態資訊", lines=4)
            
            # 影片製作
            with gr.Tab("專業影片製作"):
                gr.HTML('<div class="section"><h3 class="guide-title">AI驅動的專業營銷影片創建</h3></div>')
                
                with gr.Row():
                    with gr.Column():
                        video_title = gr.Textbox(
                            label="影片標題",
                            value="AI營銷解決方案",
                            placeholder="輸入影片主要標題"
                        )
                        video_style = gr.Dropdown(
                            label="影片風格",
                            choices=["產品展示", "品牌動畫", "促銷廣告", "企業形象"],
                            value="產品展示"
                        )
                        video_duration = gr.Slider(
                            label="影片時長 (秒)",
                            minimum=8,
                            maximum=25,
                            value=15
                        )
                        video_resolution = gr.Dropdown(
                            label="影片解析度",
                            choices=["1280x720 (HD)", "1920x1080 (Full HD)", "720x720 (方形)"],
                            value="1280x720 (HD)"
                        )
                        generate_video_btn = gr.Button("製作專業影片", variant="primary", size="lg")
                    
                    with gr.Column():
                        video_output = gr.Video(label="生成的營銷影片")
                        video_info = gr.Textbox(label="製作狀態資訊", lines=4)
            
            # 系統資訊
            with gr.Tab("系統資訊"):
                gr.HTML(f"""
                <div class="section">
                    <h3 class="guide-title">系統資訊</h3>
                    <table style="width: 100%; margin: 1.5rem 0;">
                        <tr>
                            <td>公網存取地址</td>
                            <td>
                                <code style="background: #243654; padding: 0.6rem 1rem; border-radius: 4px; color: #E0E7FF; font-family: 'SF Mono', 'Monaco', 'Cascadia Code', monospace; font-size: 0.8rem; border: 1px solid rgba(0, 191, 255, 0.2);">
                                    http://140.119.124.214:8080
                                </code>
                            </td>
                        </tr>
                        <tr>
                            <td>系統狀態</td>
                            <td><span class="status-online">ONLINE</span></td>
                        </tr>
                        <tr>
                            <td>可用功能</td>
                            <td><span class="feature-text">專業文案 | 高級圖片 | 動態影片</span></td>
                        </tr>
                        <tr>
                            <td>系統版本</td>
                            <td class="primary-text">{ai_system.version}</td>
                        </tr>
                        <tr>
                            <td>部署環境</td>
                            <td class="primary-text">生產環境 (Production)</td>
                        </tr>
                    </table>
                </div>
                
                <div class="section">
                    <h3 class="guide-title">使用指南</h3>
                    
                    <div style="margin-bottom: 1.8rem;">
                        <h4 style="color: #A478E6; font-weight: 600; font-size: 1.0rem; margin-bottom: 0.6rem;">文案生成模組</h4>
                        <ul style="color: #E0E7FF; font-size: 0.85rem; line-height: 1.6; margin-left: 0; list-style: none; padding-left: 0;">
                            <li style="margin-bottom: 0.4rem; padding-left: 1rem; position: relative;">
                                <span style="position: absolute; left: 0; color: #00BFFF;">•</span>
                                輸入產品或服務詳細資訊
                            </li>
                            <li style="margin-bottom: 0.4rem; padding-left: 1rem; position: relative;">
                                <span style="position: absolute; left: 0; color: #00BFFF;">•</span>
                                選擇適合的營銷風格
                            </li>
                            <li style="margin-bottom: 0.4rem; padding-left: 1rem; position: relative;">
                                <span style="position: absolute; left: 0; color: #00BFFF;">•</span>
                                描述目標客群和核心特色
                            </li>
                            <li style="margin-bottom: 0.4rem; padding-left: 1rem; position: relative;">
                                <span style="position: absolute; left: 0; color: #00BFFF;">•</span>
                                選擇專業或營銷語調
                            </li>
                        </ul>
                    </div>
                    
                    <div style="margin-bottom: 1.8rem;">
                        <h4 style="color: #A478E6; font-weight: 600; font-size: 1.0rem; margin-bottom: 0.6rem;">圖片設計模組</h4>
                        <ul style="color: #E0E7FF; font-size: 0.85rem; line-height: 1.6; margin-left: 0; list-style: none; padding-left: 0;">
                            <li style="margin-bottom: 0.4rem; padding-left: 1rem; position: relative;">
                                <span style="position: absolute; left: 0; color: #00BFFF;">•</span>
                                清楚描述視覺效果需求
                            </li>
                            <li style="margin-bottom: 0.4rem; padding-left: 1rem; position: relative;">
                                <span style="position: absolute; left: 0; color: #00BFFF;">•</span>
                                選擇適合用途的設計風格
                            </li>
                            <li style="margin-bottom: 0.4rem; padding-left: 1rem; position: relative;">
                                <span style="position: absolute; left: 0; color: #00BFFF;">•</span>
                                根據使用場景選擇尺寸
                            </li>
                            <li style="margin-bottom: 0.4rem; padding-left: 1rem; position: relative;">
                                <span style="position: absolute; left: 0; color: #00BFFF;">•</span>
                                調整品質以符合需求
                            </li>
                        </ul>
                    </div>
                    
                    <div style="margin-bottom: 1.8rem;">
                        <h4 style="color: #A478E6; font-weight: 600; font-size: 1.0rem; margin-bottom: 0.6rem;">影片製作模組</h4>
                        <ul style="color: #E0E7FF; font-size: 0.85rem; line-height: 1.6; margin-left: 0; list-style: none; padding-left: 0;">
                            <li style="margin-bottom: 0.4rem; padding-left: 1rem; position: relative;">
                                <span style="position: absolute; left: 0; color: #00BFFF;">•</span>
                                輸入吸引人的影片標題
                            </li>
                            <li style="margin-bottom: 0.4rem; padding-left: 1rem; position: relative;">
                                <span style="position: absolute; left: 0; color: #00BFFF;">•</span>
                                選擇符合品牌的影片風格
                            </li>
                            <li style="margin-bottom: 0.4rem; padding-left: 1rem; position: relative;">
                                <span style="position: absolute; left: 0; color: #00BFFF;">•</span>
                                設定適當的影片時長
                            </li>
                            <li style="margin-bottom: 0.4rem; padding-left: 1rem; position: relative;">
                                <span style="position: absolute; left: 0; color: #00BFFF;">•</span>
                                選擇合適的解析度
                            </li>
                        </ul>
                    </div>
                </div>
                """)
        
        # 綁定功能
        generate_content_btn.click(
            fn=ai_system.generate_content,
            inputs=[product_name, content_style, target_audience, key_features, tone_style],
            outputs=[content_output, content_info]
        )
        
        generate_image_btn.click(
            fn=ai_system.generate_image,
            inputs=[img_prompt, img_style, img_size, img_quality],
            outputs=[image_output, image_info]
        )
        
        generate_video_btn.click(
            fn=ai_system.generate_video,
            inputs=[video_title, video_style, video_duration, video_resolution],
            outputs=[video_output, video_info]
        )
    
    return demo

def check_port_availability(port):
    """檢查端口可用性"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex(('localhost', port))
            return result != 0
    except:
        return True

def start_complete_system():
    """啟動完整系統"""
    print("=" * 100)
    print("🚀 AI營銷系統 - 完整修正版")
    print("=" * 100)
    print("🌐 公網存取: http://140.119.124.214")
    print("📝 專業文案生成 ✅")
    print("🎨 高級圖片設計 ✅")
    print("🎬 動態影片製作 ✅")
    print("⚡ 狀態: 完整修正版就緒")
    print("=" * 100)
    
    demo = create_complete_interface()
    
    # 多端口啟動策略 (跳過80端口避免權限問題)
    priority_ports = [8080, 7861, 3000, 5000, 8000]
    
    for port in priority_ports:
        try:
            if not check_port_availability(port):
                print(f"⚠️ 端口 {port} 已被使用")
                continue
                
            if port == 80:
                print(f"\n🌐 啟動標準HTTP服務 - 端口 {port}")
                print("🔗 公網存取: http://140.119.124.214")
            else:
                print(f"\n🌐 啟動備用服務 - 端口 {port}")
                print(f"🔗 存取地址: http://140.119.124.214:{port}")
            
            print("🚀 系統啟動中...")
            
            # 啟動完整系統
            demo.launch(
                server_name="0.0.0.0",
                server_port=port,
                share=False,
                show_error=True,
                quiet=False,
                prevent_thread_lock=False
            )
            
            print(f"✅ 完整系統成功啟動於端口 {port}")
            print(f"🌐 公網存取: http://140.119.124.214{':'+str(port) if port != 80 else ''}")
            break
            
        except PermissionError:
            print(f"⚠️ 端口 {port} 權限不足")
            continue
            
        except OSError as e:
            if "bind" in str(e).lower():
                print(f"⚠️ 端口 {port} 地址已被使用")
            else:
                print(f"⚠️ 端口 {port} 系統錯誤: {e}")
            continue
                
        except KeyboardInterrupt:
            print("\n👋 系統已安全關閉")
            break
            
        except Exception as e:
            print(f"❌ 端口 {port} 啟動錯誤: {e}")
            if port == priority_ports[-1]:
                print("\n❌ 所有端口都無法使用")
                print("💡 建議檢查防火牆設定和端口佔用")
            continue
    else:
        print("\n❌ 系統啟動失敗")

if __name__ == "__main__":
    start_complete_system()
