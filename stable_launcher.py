#!/usr/bin/env python3
"""
完整穩定版AI營銷系統
解決網路連接問題，確保公網可存取
http://140.119.235.6 - 穩定運行
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

# 輸出目錄
output_dirs = Path("outputs")
for subdir in ["text", "images", "videos"]:
    (output_dirs / subdir).mkdir(parents=True, exist_ok=True)

class StableAISystem:
    def __init__(self):
        self.running = True
        print("🚀 穩定AI系統初始化")
        
    def generate_content(self, product, style, audience, features, tone):
        """專業文案生成"""
        try:
            templates = {
                "專業商務": {
                    "formal": f"""# {product} - 專業企業解決方案

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
                # 轉換顏色
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

def create_stable_interface():
    """創建穩定界面"""
    
    ai_system = StableAISystem()
    
    # 簡潔穩定的CSS
    css = """
    .gradio-container {
        font-family: 'Microsoft YaHei', Arial, sans-serif;
        max-width: 1200px;
        margin: 0 auto;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    .header {
        background: rgba(255,255,255,0.95);
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        margin: 1rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    .section {
        background: rgba(255,255,255,0.9);
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    """
    
    with gr.Blocks(title="AI Marketing System - Stable", theme=gr.themes.Soft(), css=css) as demo:
        
        gr.HTML("""
        <div class="header">
            <h1 style="color: #2c3e50; margin-bottom: 1rem;">🚀 AI Marketing System</h1>
            <p style="color: #7f8c8d; font-size: 1.1rem;">Complete Marketing Content Generation Platform</p>
            <div style="margin-top: 1.5rem;">
                <strong style="color: #e74c3c;">🌐 Public Access:</strong> 
                <code style="background: #ecf0f1; padding: 4px 8px; border-radius: 4px;">http://140.119.235.6</code>
            </div>
            <div style="margin-top: 0.5rem;">
                <span style="color: #27ae60; font-weight: bold;">✅ System Online & Stable</span>
            </div>
        </div>
        """)
        
        with gr.Tabs():
            # 文案生成
            with gr.Tab("📝 Content Generation"):
                gr.HTML('<div class="section"><h3>Professional Marketing Content</h3></div>')
                
                with gr.Row():
                    with gr.Column():
                        product_name = gr.Textbox(
                            label="Product Name",
                            value="Professional Solution",
                            placeholder="Enter product or service name"
                        )
                        content_style = gr.Dropdown(
                            label="Style",
                            choices=["專業商務", "創新科技", "溫馨生活"],
                            value="專業商務"
                        )
                        target_audience = gr.Textbox(
                            label="Target Audience",
                            value="Business professionals",
                            placeholder="Describe your target customers"
                        )
                        key_features = gr.Textbox(
                            label="Key Features",
                            lines=4,
                            value="• High performance\n• Professional support\n• Proven results\n• Innovation leader",
                            placeholder="List main features and benefits"
                        )
                        tone_style = gr.Radio(
                            label="Tone",
                            choices=[("Professional", "formal"), ("Persuasive", "persuasive")],
                            value="formal"
                        )
                        generate_content_btn = gr.Button("🚀 Generate Content", variant="primary")
                    
                    with gr.Column():
                        content_output = gr.Textbox(
                            label="Generated Content",
                            lines=15,
                            show_copy_button=True,
                            placeholder="Generated content will appear here..."
                        )
                        content_info = gr.Textbox(label="Status", lines=3)
            
            # 圖片設計
            with gr.Tab("🎨 Image Design"):
                gr.HTML('<div class="section"><h3>Professional Image Creation</h3></div>')
                
                with gr.Row():
                    with gr.Column():
                        img_prompt = gr.Textbox(
                            label="Description",
                            lines=2,
                            value="professional marketing design",
                            placeholder="Describe the image you want"
                        )
                        img_style = gr.Dropdown(
                            label="Style",
                            choices=["商業攝影", "創意設計", "品牌形象", "社交媒體", "印刷媒體"],
                            value="商業攝影"
                        )
                        img_size = gr.Dropdown(
                            label="Size",
                            choices=["1920x1080 (HD)", "1080x1080 (Square)", "1080x1920 (Vertical)", "1200x630 (Social)"],
                            value="1920x1080 (HD)"
                        )
                        img_quality = gr.Slider(
                            label="Quality",
                            minimum=70,
                            maximum=100,
                            value=85,
                            step=5
                        )
                        generate_image_btn = gr.Button("🎨 Create Image", variant="primary")
                    
                    with gr.Column():
                        image_output = gr.Image(label="Generated Image", height=350)
                        image_info = gr.Textbox(label="Status", lines=3)
            
            # 影片製作
            with gr.Tab("🎬 Video Production"):
                gr.HTML('<div class="section"><h3>Dynamic Video Creation</h3></div>')
                
                with gr.Row():
                    with gr.Column():
                        video_title = gr.Textbox(
                            label="Title",
                            value="Professional Solution",
                            placeholder="Enter video title"
                        )
                        video_style = gr.Dropdown(
                            label="Style",
                            choices=["產品展示", "品牌動畫", "促銷廣告", "企業形象"],
                            value="產品展示"
                        )
                        video_duration = gr.Slider(
                            label="Duration (seconds)",
                            minimum=5,
                            maximum=20,
                            value=10
                        )
                        video_resolution = gr.Dropdown(
                            label="Resolution",
                            choices=["1280x720 (HD)", "1920x1080 (Full HD)", "720x720 (Square)"],
                            value="1280x720 (HD)"
                        )
                        generate_video_btn = gr.Button("🎬 Create Video", variant="primary")
                    
                    with gr.Column():
                        video_output = gr.Video(label="Generated Video")
                        video_info = gr.Textbox(label="Status", lines=3)
            
            # 系統資訊
            with gr.Tab("ℹ️ System Info"):
                gr.HTML(f"""
                <div class="section">
                    <h3>System Status</h3>
                    <p><strong>🌐 Public URL:</strong> http://140.119.235.6</p>
                    <p><strong>📡 Server:</strong> Running on port 80</p>
                    <p><strong>⚡ Status:</strong> <span style="color: #27ae60;">Online & Stable</span></p>
                    <p><strong>🔧 Features:</strong> Text • Image • Video Generation</p>
                </div>
                
                <div class="section">
                    <h3>Usage Instructions</h3>
                    <ol>
                        <li>Select the type of content you want to generate</li>
                        <li>Fill in the required parameters</li>
                        <li>Click the generate button</li>
                        <li>Download your results</li>
                    </ol>
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

def start_stable_server():
    """啟動穩定伺服器"""
    print("=" * 80)
    print("🚀 AI MARKETING SYSTEM - STABLE VERSION")
    print("=" * 80)
    print("📝 Professional Content Generation")
    print("🎨 Advanced Image Design")  
    print("🎬 Dynamic Video Production")
    print("🌐 Public Access: http://140.119.235.6")
    print("⚡ Status: Stable & Reliable")
    print("=" * 80)
    
    demo = create_stable_interface()
    
    # 多端口嘗試策略
    ports_to_try = [80, 8080, 7861, 3000, 5000]
    
    for port in ports_to_try:
        try:
            if port == 80:
                print(f"\n🔗 嘗試標準HTTP端口 {port}")
                print("🌐 公網存取: http://140.119.235.6")
            else:
                print(f"\n🔗 嘗試備用端口 {port}")
                print(f"🌐 存取網址: http://140.119.235.6:{port}")
            
            # 啟動伺服器
            demo.launch(
                server_name="0.0.0.0",  # 允許外部存取
                server_port=port,
                share=False,           # 不使用Gradio隧道
                show_error=True,
                quiet=False,
                prevent_thread_lock=False
            )
            
            print(f"✅ 系統成功啟動於端口 {port}")
            break
            
        except (PermissionError, OSError) as e:
            if "bind" in str(e).lower() or "address already in use" in str(e).lower():
                print(f"⚠️ 端口 {port} 已被使用，嘗試下一個端口")
            elif "permission denied" in str(e).lower():
                print(f"⚠️ 端口 {port} 權限不足，嘗試下一個端口") 
            else:
                print(f"⚠️ 端口 {port} 啟動失敗: {e}")
                
            if port == ports_to_try[-1]:
                print("\n❌ 所有端口都無法使用")
                print("💡 建議檢查:")
                print("   1. 防火牆設定")
                print("   2. 端口佔用情況") 
                print("   3. 管理員權限")
                break
            continue
            
        except KeyboardInterrupt:
            print("\n👋 系統已安全關閉")
            break
            
        except Exception as e:
            print(f"❌ 未預期錯誤: {e}")
            if port == ports_to_try[-1]:
                print("❌ 系統啟動失敗")
                break
            continue

if __name__ == "__main__":
    start_stable_server()