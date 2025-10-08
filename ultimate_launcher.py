#!/usr/bin/env python3#!/usr/bin/env python3

""""""

AI營銷內容生成系統 - 完整專業版AI營銷內容生成系統 - 快速完整版

支持文字、圖片、影片生成的企業級解決方案整合真實AI模型的圖像和影片生成功能

""""""



import gradio as grimport gradio as gr

import osimport os

import sysimport time

import torchimport datetime

import cv2from pathlib import Path

import numpy as npimport traceback

from PIL import Image, ImageDraw, ImageFontimport subprocess

from pathlib import Pathimport sys

from datetime import datetime

import json# 創建輸出目錄

import randomoutput_dir = Path("outputs")

output_dir.mkdir(exist_ok=True)

# 基本設置(output_dir / "text").mkdir(exist_ok=True)

BASE_DIR = Path(__file__).parent(output_dir / "images").mkdir(exist_ok=True)

OUTPUTS_DIR = BASE_DIR / "outputs"(output_dir / "videos").mkdir(exist_ok=True)

for subdir in ["text", "images", "videos"]:

    (OUTPUTS_DIR / subdir).mkdir(parents=True, exist_ok=True)def check_and_install_dependencies():

    """檢查並安裝必要依賴"""

class CompleteAIMarketing:    try:

    """完整的AI營銷系統"""        import torch

            import diffusers

    def __init__(self):        return True

        self.device = "cuda" if torch.cuda.is_available() else "cpu"    except ImportError:

        self.sdxl_pipeline = None        return False

        print(f"🔧 初始化系統 - 設備: {self.device.upper()}")

        self.load_ai_models()def generate_text_advanced(product_name, ta    print("🌐 配置公網訪問模式...")

        print("🔗 本地訪問: http://localhost:7861")

    def load_ai_models(self):    print("🔗 公網訪問: http://140.119.235.6:7861")

        """載入AI模型"""    print("💡 確保防火牆已開放7861端口")

        try:    print("=" * 80)

            from diffusers import StableDiffusionXLPipeline    

            model_path = BASE_DIR / "checkpoints" / "sdxl-base-1.0"    demo.launch(

                    server_name="0.0.0.0",  # 監聽所有網絡接口，支持公網訪問

            if model_path.exists():        server_port=7861,

                print("✅ 載入本地SDXL模型...")        share=False,

                self.sdxl_pipeline = StableDiffusionXLPipeline.from_pretrained(        show_error=True,  # 顯示錯誤便於調試

                    str(model_path),        quiet=True,  # 減少輸出

                    torch_dtype=torch.float16 if self.device == "cuda" else torch.float32        inbrowser=False,

                )        auth=auth_config,

                if self.device == "cuda":        prevent_thread_lock=False

                    self.sdxl_pipeline = self.sdxl_pipeline.to(self.device)    )ontent_type, tone="專業", language="繁體中文"):

                print("✅ SDXL模型載入成功")    """高級文案生成功能"""

            else:    try:

                print("⚠️ 本地模型未找到，將使用占位功能")        if not product_name.strip():

        except Exception as e:            return "❌ 請輸入產品名稱", ""

            print(f"⚠️ AI模型載入異常: {e}")        

            print("🔄 系統將正常運行，使用替代功能")        # 使用更豐富的模板系統

            advanced_templates = {

    def generate_professional_content(self, product_name, content_style, target_audience, key_features, tone_style):            "產品介紹": {

        """生成專業營銷內容"""                "專業": f"""## ✨ {product_name} - 專業級解決方案

        

        # 高質量文案模板### 🎯 專為{target_audience}設計

        templates = {{product_name}是一款專門為{target_audience}量身打造的創新產品，融合了最新技術與人性化設計理念。

            "專業商務": {

                "formal": f"""# {product_name} - 企業級解決方案### 🌟 核心優勢

- **🔬 尖端技術**: 採用業界領先的先進技術

## 產品核心價值- **💎 卓越品質**: 嚴格品控，確保每一件產品都達到最高標準  

{key_features}- **🎨 精美設計**: 由頂尖設計師團隊精心打造

- **🛡️ 安全可靠**: 通過多重安全認證，使用更安心

## 目標市場定位- **🌱 環保責任**: 採用可持續材料，關愛地球

專為 {target_audience} 精心設計的專業解決方案

### 📈 市場認可

## 競爭優勢分析自上市以來，{product_name}已獲得超過10萬名{target_audience}的信賴與好評，在同類產品中脫穎而出。

• **品質保證**: 通過國際標準認證，品質值得信賴

• **技術支持**: 提供7×24小時專業技術服務### 🚀 立即體驗

• **性價比優勢**: 同等品質下最具競爭力的價格選擇{product_name}，就是選擇品質與創新。讓我們一起開創更美好的未來！

• **客戶案例**: 已成功服務超過1000+企業客戶

*#{product_name} #專業品質 #創新科技 #用戶首選*""",

## 立即行動

**聯繫我們獲取專業諮詢與定制方案**                "親切": f"""💫 嗨！{target_audience}朋友們！

📞 業務專線 | 📧 企業郵箱 | 🌐 官方網站""",

想跟大家分享一個超棒的發現 - {product_name}！💕

                "persuasive": f"""🎯 **{product_name}** - 領先市場的明智選擇

🤗 **為什麼我們愛上了它？**

✨ **為什麼超過10萬用戶選擇我們？**還記得那些讓人頭疼的日常問題嗎？{product_name}就像是專門為我們{target_audience}準備的貼心小幫手！

{key_features}

✨ **它有什麼特別的？**

👥 **{target_audience}的首選品牌**- 💝 就像好朋友一樣貼心 - 懂你所需

我們深度理解您的需求，提供超出期望的解決方案- 🌈 色彩繽紛的設計 - 每天都有好心情

- 🎉 操作超簡單 - 連我媽媽都說讚！

🏆 **限時優惠，立即行動的3大理由：**- 💪 品質超棒 - 用過就回不去了

• 🎁 新客戶專享85折優惠，省下真金白銀- 🌿 環保材質 - 愛自己也愛地球

• 🚀 免費試用30天，零風險體驗產品價值  

• 🏅 行業領先技術，助您在競爭中脫穎而出👥 **大家都在說...**

"用了{product_name}之後，生活真的變得更輕鬆了！" - 滿意用戶小美

**機會難得，現在就加入成功者的行列！**"強烈推薦給所有{target_audience}！" - 資深用戶阿明

點擊立即諮詢，專業顧問為您量身規劃"""

            },💖 **一起加入{product_name}的大家庭吧！**

            讓我們用{product_name}，讓每一天都更美好！

            "創新科技": {

                "formal": f"""# {product_name} - 引領科技創新*#{product_name} #生活好物 #推薦 #幸福生活*"""

            },

## 技術創新突破            

{key_features}            "廣告文案": {

                "專業": f"""🚨 **重磅發布！{product_name}正式上市** 🚨

## 應用場景分析

針對 {target_audience} 的數位化轉型需求### 🎉 限時首發優惠

- 💰 **早鳥特價**: 限時85折優惠

## 核心技術優勢  - 🚚 **免費配送**: 全台24小時快速到貨  

• **AI驅動**: 採用最新人工智能算法，效能提升300%- 🔄 **品質保證**: 30天不滿意無條件退換

• **雲端整合**: 無縫整合雲端服務，數據安全可靠- 🎁 **專屬禮包**: 首批用戶獨享精美配件

• **智能分析**: 深度學習技術，提供精準數據洞察

• **可擴展性**: 模組化設計，隨業務成長靈活擴展### 🎯 為{target_audience}量身打造

歷經18個月研發，邀請超過500名{target_audience}參與測試，{product_name}集合了所有您期待的功能與體驗。

## 科技賦能未來

**體驗下一代科技解決方案**""",### ⭐ 用戶真實評價

★★★★★ "這是我用過最棒的產品！" - 資深用戶

                "persuasive": f"""🚀 **{product_name}** - 未來科技，現在擁有！★★★★★ "完全超出預期，強烈推薦！" - 滿意顧客

★★★★★ "CP值超高，買到賺到！" - 忠實粉絲

⚡ **革命性突破，改變遊戲規則：**

{key_features}### ⏰ 限量搶購中

首批僅限1000個名額，售完即恢復原價！

🤖 **為 {target_audience} 打造的智能化體驗**

科技不應該複雜，我們讓創新變得簡單易用### 🛒 立即下單

點擊下方連結，馬上擁有{product_name}！

🔥 **搶先體驗未來科技的3大優勢：**

• 🎯 早鳥用戶享受6折特價，錯過再等一年**🔥 現在下單，享受全年最低價！**

• 🆓 終身免費升級服務，投資一次受益永久

• 👨‍💻 一對一專家培訓，快速掌握核心技能*#{product_name} #{target_audience} #限時特惠 #搶購中*""",

                

**科技革命已經來臨，現在加入還不算晚！**                "活潑": f"""🎉🎊 超級大消息！{product_name}來啦！ 🎊🎉

立即預約演示，親眼見證未來"""

            },🚀 **{target_audience}專屬好康來了！**

            

            "溫馨生活": {😍 還在煩惱每天的小困擾嗎？

                "formal": f"""{product_name} - 品質生活的最佳選擇😎 {product_name}來拯救你的生活啦！



為家庭帶來更美好的生活體驗🎈 **首發超殺優惠** 🎈

{key_features}🔥 限時7折 - 錯過再等一年！

🎁 買就送價值千元好禮

專為 {target_audience} 設計的生活解決方案📦 24小時火速到貨

💝 不滿意秒退款

品質承諾：

• **安全保障**: 採用環保材料，通過安全檢測認證🌟 **用過的都說讚！**

• **人性設計**: 考慮使用者習慣，提供舒適體驗🗣️ "哇！太神奇了！" - 驚豔用戶

• **耐用可靠**: 嚴格品質控制，使用壽命超出預期  🗣️ "早該發現這個寶貝！" - 後悔用戶  

• **售後服務**: 完善的客戶服務體系，使用無憂🗣️ "已經推薦給所有朋友！" - 忠實粉絲



讓家更溫暖，讓生活更美好""",⚡ **衝衝衝！機會稍縱即逝！**

只有7天！只有1000個！賣完就沒了！

                "persuasive": f"""❤️ **{product_name}** - 給家人最好的愛

🛒 **馬上搶購** 👈 點這裡！

🏠 **為您和家人帶來的美好改變：**

{key_features}#{product_name} #好康推推 #限時搶購 #錯過可惜"""

            },

👨‍👩‍👧‍👦 **{target_audience}都在使用的生活好幫手**            

因為愛家，所以選擇最好的            "社交媒體": {

                "活潑": f"""📱 【{product_name}震撼登場！】

💝 **限量優惠，錯過可惜：**

• 🛒 家庭裝8折優惠，平均每天不到一杯咖啡錢{target_audience}集合！你們等待的神器終於來了！🔥

• 💯 100%滿意保證，30天不滿意全額退款

• 🎁 現在下單贈送價值299元的配件大禮包✨ **3秒愛上它的理由：**

1️⃣ 超高CP值 - 花小錢享大品質

**愛要行動，給家人最貼心的關懷！**2️⃣ 簡單好用 - 3歲到80歲都會用

數量有限，售完即止"""3️⃣ 效果驚人 - 用過就回不去系列

            }

        }🎯 **特別企劃**

        💫 新用戶專享88折

        # 選擇合適的模板🚀 分享再送神秘禮物

        style_templates = templates.get(content_style, templates["專業商務"])💝 評價還能抽大獎

        content = style_templates.get(tone_style, style_templates["formal"])

        📸 **曬照抽獎活動**

        # 保存文件用{product_name}拍照上傳，tag 3個好友

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")週週抽出幸運兒送iPhone！📱

        filename = f"marketing_content_{timestamp}.txt"

        filepath = OUTPUTS_DIR / "text" / filename💬 **留言區熱烈討論中**

        你最期待{product_name}的哪個功能？

        with open(filepath, 'w', encoding='utf-8') as f:留言告訴我們，小編會親自回覆哦～

            f.write(content)

        👆 雙擊愛心 + 分享，讓更多人知道這個好消息！

        info_text = f"✅ 內容生成完成\n📄 文件: {filename}\n🎨 風格: {content_style}\n📝 語調: {tone_style}\n📊 字數: {len(content)}"

        #{product_name} #必買好物 #限時活動 #分享抽獎"""

        return content, info_text            }

            }

    def create_professional_image(self, description, visual_style, dimensions, quality_steps, guidance_scale):        

        """生成專業圖片"""        # 選擇模板

                template_group = advanced_templates.get(content_type, advanced_templates["產品介紹"])

        if self.sdxl_pipeline:        template = template_group.get(tone, list(template_group.values())[0])

            return self._generate_sdxl_image(description, visual_style, dimensions, quality_steps, guidance_scale)        

        else:        # 保存結果

            return self._create_premium_placeholder(description, visual_style, dimensions)        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

            filename = f"text_{timestamp}.txt"

    def _generate_sdxl_image(self, description, visual_style, dimensions, quality_steps, guidance_scale):        filepath = output_dir / "text" / filename

        """使用SDXL生成真實圖片"""        

        try:        with open(filepath, 'w', encoding='utf-8') as f:

            width, height = map(int, dimensions.split('x'))            f.write(f"=== AI營銷文案生成結果 ===\n\n")

                        f.write(f"產品名稱: {product_name}\n")

            # 專業風格提示詞            f.write(f"目標受眾: {target_audience}\n")

            style_enhance = {            f.write(f"內容類型: {content_type}\n")

                "商業攝影": "professional commercial photography, studio lighting, high-end product shot, clean composition, 8k ultra detailed",            f.write(f"語調風格: {tone}\n")

                "創意設計": "creative professional design, modern aesthetic, minimalist composition, artistic layout, award-winning design",            f.write(f"語言: {language}\n")

                "品牌形象": "premium brand photography, luxury aesthetic, corporate identity, professional branding, elegant composition",            f.write(f"生成時間: {datetime.datetime.now()}\n")

                "社交媒體": "social media optimized, engaging visual design, modern trendy style, eye-catching composition, viral potential",            f.write(f"字數: {len(template)} 字\n\n")

                "印刷媒體": "print-ready professional photography, editorial quality, high resolution commercial shot, publication standard"            f.write("="*50 + "\n\n")

            }            f.write(template)

                    

            enhanced_prompt = f"{description}, {style_enhance.get(visual_style, style_enhance['商業攝影'])}"        status = f"✅ 文案生成成功！\n📁 已保存至: {filename}\n📊 字數: {len(template)} 字\n⭐ 高級模板系統"

                    return template, status

            print(f"🎨 正在生成高品質圖片...")        

                except Exception as e:

            # AI圖片生成        return f"❌ 生成失敗: {str(e)}", f"錯誤詳情: {traceback.format_exc()}"

            with torch.autocast(self.device):

                generated_image = self.sdxl_pipeline(def generate_image_with_diffusers(prompt, style="photography", size="1024x1024", quality="standard"):

                    prompt=enhanced_prompt,    """使用Diffusers生成圖像"""

                    negative_prompt="low quality, blurry, amateur, distorted, watermark, text, signature",    try:

                    width=width,        # 檢查依賴

                    height=height,        if not check_and_install_dependencies():

                    num_inference_steps=quality_steps,            return None, "❌ 請先安裝必要依賴: pip install torch diffusers"

                    guidance_scale=guidance_scale        

                ).images[0]        import torch

                    from diffusers import StableDiffusionXLPipeline

            # 保存圖片        import PIL.Image

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")        

            filename = f"professional_image_{timestamp}.png"        # 檢查模型是否存在

            filepath = OUTPUTS_DIR / "images" / filename        model_path = Path("checkpoints/sdxl-base-1.0")

            generated_image.save(filepath)        if not model_path.exists():

                        return None, "❌ SDXL模型未找到，請先運行: python download_models.py"

            info_text = f"✅ AI圖片生成成功\n📄 檔案: {filename}\n📐 尺寸: {dimensions}\n🎨 風格: {visual_style}\n⚙️ 品質: {quality_steps} steps"        

                    # 風格映射

            return str(filepath), info_text        style_prompts = {

                        "photography": "professional product photography, studio lighting, high resolution, 4K",

        except Exception as e:            "digital-art": "digital art, concept art, artstation trending, highly detailed",

            print(f"❌ SDXL生成失敗: {e}")            "cinematic": "cinematic lighting, movie poster style, dramatic, epic",

            return self._create_premium_placeholder(description, visual_style, dimensions)            "anime": "anime style, manga art, vibrant colors, detailed",

                "fantasy-art": "fantasy art, magical, mystical, enchanted",

    def _create_premium_placeholder(self, description, visual_style, dimensions):            "comic-book": "comic book style, pop art, bold colors, graphic novel"

        """創建高品質占位圖"""        }

        try:        

            width, height = map(int, dimensions.split('x'))        # 增強提示詞

                    enhanced_prompt = f"{prompt}, {style_prompts.get(style, style_prompts['photography'])}"

            # 專業配色方案        

            color_palettes = {        # 設置參數

                "商業攝影": {"primary": "#2c3e50", "secondary": "#3498db", "bg": "#ecf0f1", "text": "#2c3e50"},        width, height = [int(x) for x in size.split('x')]

                "創意設計": {"primary": "#9b59b6", "secondary": "#e74c3c", "bg": "#ffffff", "text": "#2c3e50"},         steps = {"draft": 15, "standard": 25, "premium": 35}.get(quality, 25)

                "品牌形象": {"primary": "#34495e", "secondary": "#f39c12", "bg": "#f8f9fa", "text": "#2c3e50"},        

                "社交媒體": {"primary": "#e91e63", "secondary": "#00bcd4", "bg": "#fafafa", "text": "#333333"},        print(f"Image Generation: {enhanced_prompt}")

                "印刷媒體": {"primary": "#1976d2", "secondary": "#ffc107", "bg": "#f5f5f5", "text": "#424242"}        print(f"Dimensions: {width}x{height}, Steps: {steps}")

            }        

                    # 載入模型

            colors = color_palettes.get(visual_style, color_palettes["商業攝影"])        pipe = StableDiffusionXLPipeline.from_pretrained(

                        str(model_path),

            # 創建圖片            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,

            img = Image.new('RGB', (width, height), color=colors["bg"])            use_safetensors=True,

            draw = ImageDraw.Draw(img)            variant="fp16" if torch.cuda.is_available() else None

                    )

            # 添加專業漸變效果        

            for y in range(height):        if torch.cuda.is_available():

                alpha = y / height * 0.15            pipe = pipe.to("cuda")

                gradient_r = int(int(colors["bg"][1:3], 16) * (1-alpha) + int(colors["secondary"][1:3], 16) * alpha)            print("GPU Acceleration: Enabled")

                gradient_g = int(int(colors["bg"][3:5], 16) * (1-alpha) + int(colors["secondary"][3:5], 16) * alpha)          else:

                gradient_b = int(int(colors["bg"][5:7], 16) * (1-alpha) + int(colors["secondary"][5:7], 16) * alpha)            print("Processing Mode: CPU (Slower Performance)")

                        

                draw.line([(0, y), (width, y)], fill=(gradient_r, gradient_g, gradient_b))        # 生成圖像

                    image = pipe(

            # 繪製專業內容            prompt=enhanced_prompt,

            center_x, center_y = width // 2, height // 2            width=width,

                        height=height,

            # 主標題            num_inference_steps=steps,

            title = "AI Marketing Generator"            guidance_scale=7.5,

            font_size = min(width, height) // 20            negative_prompt="blurry, low quality, distorted, ugly, bad anatomy"

            try:        ).images[0]

                font_large = ImageFont.load_default()        

            except:        # 保存圖像

                font_large = None        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

                    filename = f"image_{timestamp}.png"

            if font_large:        filepath = output_dir / "images" / filename

                # 計算文字位置        

                bbox = draw.textbbox((0, 0), title, font=font_large)        image.save(filepath, quality=95)

                text_width = bbox[2] - bbox[0]        

                draw.text((center_x - text_width//2, center_y - 80), title, fill=colors["primary"], font=font_large)        status = f"""✅ 圖像生成成功！

            📁 保存路徑: {filename}

            # 風格標籤🎨 風格: {style}

            style_text = f"Style: {visual_style}"📐 尺寸: {width}x{height}

            if font_large:⚙️ 質量: {quality}

                bbox = draw.textbbox((0, 0), style_text, font=font_large)🖼️ 提示詞: {enhanced_prompt[:100]}..."""

                text_width = bbox[2] - bbox[0]        

                draw.text((center_x - text_width//2, center_y - 40), style_text, fill=colors["text"], font=font_large)        return str(filepath), status

                    

            # 描述預覽    except Exception as e:

            desc_preview = description[:40] + "..." if len(description) > 40 else description        error_msg = f"❌ 圖像生成失敗: {str(e)}"

            desc_text = f'"{desc_preview}"'        return None, f"{error_msg}\n\n詳細錯誤:\n{traceback.format_exc()}"

            if font_large:

                bbox = draw.textbbox((0, 0), desc_text, font=font_large)def generate_video_from_image(image_path, style="smooth", duration=4, fps=24):

                text_width = bbox[2] - bbox[0]    """從圖像生成影片"""

                draw.text((center_x - text_width//2, center_y + 20), desc_text, fill=colors["text"], font=font_large)    try:

                    if not image_path:

            # 品質標識            return None, "❌ 請先上傳圖像或生成圖像"

            quality_text = "Professional Quality Placeholder"        

            if font_large:        # 檢查依賴

                bbox = draw.textbbox((0, 0), quality_text, font=font_large)        try:

                text_width = bbox[2] - bbox[0]            import cv2

                draw.text((center_x - text_width//2, center_y + 80), quality_text, fill=colors["secondary"], font=font_large)            import numpy as np

                        from PIL import Image

            # 添加專業邊框        except ImportError:

            border_width = max(3, min(width, height) // 200)            return None, "❌ 請安裝依賴: pip install opencv-python pillow"

            draw.rectangle([border_width, border_width, width-border_width, height-border_width],         

                          outline=colors["primary"], width=border_width)        # 檢查輸入圖像

                    if not os.path.exists(image_path):

            # 保存文件            return None, "❌ 圖像文件不存在"

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")        

            filename = f"professional_placeholder_{timestamp}.png"        print(f"Video Generation: {style} Style, {duration} Seconds")

            filepath = OUTPUTS_DIR / "images" / filename        

            img.save(filepath)        # 載入圖像

                    img = cv2.imread(image_path)

            info_text = f"✅ 專業占位圖片已生成\n📄 檔案: {filename}\n📐 尺寸: {dimensions}\n🎨 風格: {visual_style}\n💡 提示: 安裝SDXL模型可生成AI圖片"        if img is None:

                        return None, "❌ 無法讀取圖像文件"

            return str(filepath), info_text        

                    height, width = img.shape[:2]

        except Exception as e:        

            # 基礎fallback        # 創建影片寫入器

            basic_img = Image.new('RGB', (512, 512), '#f0f0f0')        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

            basic_path = OUTPUTS_DIR / "images" / "basic.png"        filename = f"video_{timestamp}.mp4"

            basic_img.save(basic_path)        filepath = output_dir / "videos" / filename

            return str(basic_path), f"⚠️ 基礎圖片生成: {e}"        

            fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    def create_marketing_video(self, product_title, video_category, duration_seconds, video_resolution):        out = cv2.VideoWriter(str(filepath), fourcc, fps, (width, height))

        """生成營銷影片"""        

        try:        total_frames = duration * fps

            width, height = map(int, video_resolution.split('x'))        

            fps = 30        # 生成動畫幀

            total_frames = duration_seconds * fps        for frame_num in range(total_frames):

                        progress = frame_num / total_frames

            print(f"🎬 生成專業營銷影片: {product_title}")            

                        if style == "smooth":

            # 設置影片編碼                # 平滑縮放效果

            fourcc = cv2.VideoWriter_fourcc(*'mp4v')                scale = 1.0 + 0.1 * np.sin(2 * np.pi * progress)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")                center = (width // 2, height // 2)

            filename = f"marketing_video_{timestamp}.mp4"                matrix = cv2.getRotationMatrix2D(center, 0, scale)

            filepath = OUTPUTS_DIR / "videos" / filename                frame = cv2.warpAffine(img, matrix, (width, height))

                            

            video_writer = cv2.VideoWriter(str(filepath), fourcc, fps, (width, height))            elif style == "rotation":

                            # 旋轉效果

            # 根據類別生成不同風格影片                angle = 360 * progress

            if video_category == "產品展示":                center = (width // 2, height // 2)

                self._generate_product_showcase_video(video_writer, product_title, total_frames, width, height)                matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

            elif video_category == "品牌動畫":                  frame = cv2.warpAffine(img, matrix, (width, height))

                self._generate_brand_animation_video(video_writer, product_title, total_frames, width, height)                

            elif video_category == "促銷廣告":            elif style == "zoom":

                self._generate_promotional_video(video_writer, product_title, total_frames, width, height)                # 縮放效果

                            scale = 1.0 + 0.5 * progress

            video_writer.release()                center = (width // 2, height // 2)

                            matrix = cv2.getRotationMatrix2D(center, 0, scale)

            info_text = f"✅ 影片生成完成\n📄 檔案: {filename}\n🎬 時長: {duration_seconds}秒\n📺 解析度: {video_resolution}\n🎨 類型: {video_category}"                frame = cv2.warpAffine(img, matrix, (width, height))

                            

            return str(filepath), info_text            elif style == "fade":

                            # 淡入淡出效果

        except Exception as e:                alpha = 0.5 + 0.5 * np.sin(2 * np.pi * progress)

            print(f"❌ 影片生成失敗: {e}")                frame = cv2.addWeighted(img, alpha, np.zeros_like(img), 1-alpha, 0)

            return None, f"❌ 影片生成錯誤: {str(e)}"                

                else:

    def _generate_product_showcase_video(self, writer, title, frames, width, height):                # 預設：靜態圖像

        """產品展示影片"""                frame = img.copy()

        for frame_idx in range(frames):            

            progress = frame_idx / frames            out.write(frame)

                    

            # 專業漸變背景        out.release()

            img = np.zeros((height, width, 3), dtype=np.uint8)        

            for y in range(height):        # 獲取文件大小

                gradient_value = int(245 - (y / height) * 45 + np.sin(progress * np.pi * 2) * 15)        file_size = os.path.getsize(filepath) / (1024 * 1024)  # MB

                img[y, :] = [gradient_value-20, gradient_value-10, gradient_value]        

                    status = f"""✅ 影片生成成功！

            # 標題動畫📁 保存路徑: {filename}  

            font = cv2.FONT_HERSHEY_SIMPLEX🎬 動畫風格: {style}

            ⏱️ 時長: {duration}秒

            # 主標題帶動畫效果🎥 幀率: {fps} FPS

            scale_factor = 2.0 + np.sin(progress * np.pi * 4) * 0.1📊 文件大小: {file_size:.1f}MB

            title_size = cv2.getTextSize(title, font, scale_factor, 3)[0]🖼️ 解析度: {width}x{height}"""

            title_x = (width - title_size[0]) // 2        

            title_y = height // 2 - 60        return str(filepath), status

                    

            # 淡入效果    except Exception as e:

            alpha = min(1.0, progress * 2.5)        error_msg = f"❌ 影片生成失敗: {str(e)}"

            if alpha > 0:        return None, f"{error_msg}\n\n詳細錯誤:\n{traceback.format_exc()}"

                cv2.putText(img, title, (title_x, title_y), font, scale_factor, (40, 40, 180), 3)

            # 創建Gradio界面

            # 副標題def create_complete_interface():

            subtitle = "Professional Product Presentation"    """創建完整功能界面"""

            if progress > 0.3:    

                sub_size = cv2.getTextSize(subtitle, font, 1.0, 2)[0]    with gr.Blocks(

                sub_x = (width - sub_size[0]) // 2        title="AI營銷內容生成系統 - 完整版",

                sub_y = title_y + 80        theme=gr.themes.Base()

                cv2.putText(img, subtitle, (sub_x, sub_y), font, 1.0, (80, 80, 120), 2)    ) as demo:

                    

            # 裝飾性動畫元素        gr.HTML("""

            if progress > 0.5:        <div style="text-align: center; background: linear-gradient(135deg, #2c3e50 0%, #3498db 50%, #9b59b6 100%); color: white; padding: 40px; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); border: 1px solid rgba(255,255,255,0.1);">

                center_x, center_y = width // 2, height // 2 + 120            <h1 style="margin: 0; font-size: 2.8em; font-weight: 300; letter-spacing: 2px; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">AI MARKETING SUITE</h1>

                for i in range(8):            <h2 style="margin: 15px 0; opacity: 0.9; font-weight: 300; font-size: 1.3em;">企業級營銷內容生成平台</h2>

                    angle = progress * 360 + i * 45            <p style="margin: 0; font-size: 1.1em; opacity: 0.8; font-weight: 300;">智能文案創作 | 專業圖像設計 | 動態影片製作 | 一站式解決方案</p>

                    radius = 50 + i * 10        </div>

                    x = int(center_x + radius * np.cos(np.radians(angle)))        """)

                    y = int(center_y + radius * np.sin(np.radians(angle)))        

                    cv2.circle(img, (x, y), 6, (100 + i*15, 80, 180), -1)        with gr.Tabs() as tabs:

                        # 文案生成標籤

            # 專業邊框            with gr.Tab("智能文案生成"):

            border_color = (120, 100, 160)                with gr.Row():

            cv2.rectangle(img, (20, 20), (width-20, height-20), border_color, 4)                    with gr.Column():

                                    gr.Markdown("### 文案創作設定", elem_classes="professional-header")

            writer.write(img)                        

                            product_name = gr.Textbox(

    def _generate_brand_animation_video(self, writer, title, frames, width, height):                            label="產品名稱",

        """品牌動畫影片"""                            placeholder="輸入您的產品名稱，例如：智能手錶、環保水杯、健身APP...",

        for frame_idx in range(frames):                            lines=1

            progress = frame_idx / frames                        )

            img = np.zeros((height, width, 3), dtype=np.uint8)                        

                                    target_audience = gr.Textbox(

            center_x, center_y = width // 2, height // 2                            label="目標受眾", 

                                        placeholder="描述您的目標客戶，例如：25-35歲都市上班族、健身愛好者...",

            # 多層動畫圓環                            lines=1

            for ring in range(6):                        )

                radius = int(25 + ring * 35 + progress * 120 - ring * 15)                        

                if radius > 0 and radius < min(width, height) // 2:                        with gr.Row():

                    intensity = int(200 - ring * 25 - progress * 50)                            content_type = gr.Dropdown(

                    intensity = max(50, min(255, intensity))                                choices=["產品介紹", "廣告文案", "社交媒體", "新聞稿", "電子郵件"],

                                                    label="內容類型",

                    color = (intensity//4, intensity//2, intensity)                                value="產品介紹"

                    cv2.circle(img, (center_x, center_y), radius, color, 3)                            )

                                        

            # 品牌標題動畫                            tone = gr.Dropdown(

            font = cv2.FONT_HERSHEY_SIMPLEX                                choices=["專業", "親切", "活潑", "正式", "幽默"],

            text_scale = 1.8 + np.sin(progress * np.pi * 6) * 0.2                                label="語調風格",

                                            value="專業"

            text_size = cv2.getTextSize(title, font, text_scale, 3)[0]                            )

            text_x = (width - text_size[0]) // 2                        

            text_y = (height + text_size[1]) // 2                        language = gr.Dropdown(

                                        choices=["繁體中文", "簡體中文", "English", "日本語"],

            # 動態顏色                            label="輸出語言",

            color_r = int(220 + 35 * np.sin(progress * np.pi * 3))                            value="繁體中文"

            color_g = int(180 + 35 * np.cos(progress * np.pi * 3))                        )

            color_b = 255                        

                                    text_btn = gr.Button("生成文案", variant="primary", size="lg")

            cv2.putText(img, title, (text_x, text_y), font, text_scale, (color_r, color_g, color_b), 3)                    

                                with gr.Column():

            # 品牌標語                        gr.Markdown("### 生成結果", elem_classes="professional-header")

            if progress > 0.4:                        

                tagline = "Innovation & Excellence"                        text_output = gr.Textbox(

                tag_size = cv2.getTextSize(tagline, font, 0.9, 2)[0]                            label="AI生成的營銷文案",

                tag_x = (width - tag_size[0]) // 2                            lines=20,

                tag_y = text_y + 70                            show_copy_button=True,

                cv2.putText(img, tagline, (tag_x, tag_y), font, 0.9, (180, 180, 220), 2)                            placeholder="生成的文案內容將在此顯示..."

                                    )

            writer.write(img)                        

                            text_status = gr.Textbox(

    def _generate_promotional_video(self, writer, title, frames, width, height):                            label="生成狀態",

        """促銷廣告影片"""                            lines=4,

        for frame_idx in range(frames):                            interactive=False

            flash_cycle = frame_idx % 30                        )

            base_intensity = 60 + (flash_cycle % 15) * 12            

                        # 圖像生成標籤  

            # 動態背景            with gr.Tab("AI圖像生成"):

            img = np.full((height, width, 3), base_intensity//2, dtype=np.uint8)                with gr.Row():

                                with gr.Column():

            # 添加動態條紋                        gr.Markdown("### 圖像生成設定", elem_classes="professional-header")

            for stripe in range(0, height, 50):                        

                stripe_color = base_intensity + 40                        image_prompt = gr.Textbox(

                cv2.rectangle(img, (0, stripe), (width, stripe + 25), (stripe_color//4, stripe_color//3, stripe_color//2), -1)                            label="圖像描述提示詞",

                                        placeholder="詳細描述您想要的圖像，例如：現代簡約風格的智能手錶產品攝影，白色背景，專業打光，高畫質...",

            font = cv2.FONT_HERSHEY_SIMPLEX                            lines=4

            progress = frame_idx / frames                        )

                                    

            # 主產品標題                        with gr.Row():

            main_scale = 2.2 + np.sin(progress * np.pi * 8) * 0.3                            image_style = gr.Dropdown(

            main_size = cv2.getTextSize(title, font, main_scale, 4)[0]                                choices=["photography", "digital-art", "cinematic", "anime", "fantasy-art", "comic-book"],

            main_x = (width - main_size[0]) // 2                                label="藝術風格",

            main_y = height // 2 - 100                                value="photography"

                                        )

            if flash_cycle < 20:  # 閃爍效果                            

                cv2.putText(img, title, (main_x, main_y), font, main_scale, (255, 255, 100), 4)                            image_size = gr.Dropdown(

                                                choices=["1024x1024", "1024x768", "768x1024", "1344x768", "768x1344"],

                # 促銷標語                                label="圖像尺寸",

                promo_messages = ["LIMITED OFFER!", "EXCLUSIVE DEAL!", "ACT NOW!"]                                value="1024x1024"

                current_msg = promo_messages[frame_idx // 20 % len(promo_messages)]                            )

                                        

                promo_size = cv2.getTextSize(current_msg, font, 1.4, 3)[0]                        image_quality = gr.Dropdown(

                promo_x = (width - promo_size[0]) // 2                            choices=["draft", "standard", "premium"],

                promo_y = main_y + 90                            label="生成質量",

                                            value="standard"

                cv2.putText(img, current_msg, (promo_x, promo_y), font, 1.4, (255, 50, 50), 3)                        )

                                        

                # 折扣資訊                        image_btn = gr.Button("生成圖像", variant="primary", size="lg")

                if progress > 0.25:                    

                    discount_text = "UP TO 50% OFF!"                    with gr.Column():

                    disc_size = cv2.getTextSize(discount_text, font, 1.1, 3)[0]                        gr.Markdown("### 生成結果", elem_classes="professional-header")

                    disc_x = (width - disc_size[0]) // 2                        

                    disc_y = promo_y + 80                        image_output = gr.Image(

                                                label="AI生成的圖像",

                    # 折扣背景框                            type="filepath",

                    cv2.rectangle(img, (disc_x - 25, disc_y - 45), (disc_x + disc_size[0] + 25, disc_y + 15), (50, 180, 50), -1)                            height=400

                    cv2.putText(img, discount_text, (disc_x, disc_y), font, 1.1, (255, 255, 255), 3)                        )

                                    

            writer.write(img)                        image_status = gr.Textbox(

                            label="生成狀態",

def create_complete_professional_interface():                            lines=6,

    """創建完整的專業界面"""                            interactive=False

                            )

    # 初始化系統            

    ai_system = CompleteAIMarketing()            # 影片生成標籤

                with gr.Tab("AI影片生成"):

    # 專業CSS樣式                with gr.Row():

    professional_css = """                    with gr.Column():

    .gradio-container {                        gr.Markdown("### 影片生成設定", elem_classes="professional-header")

        font-family: 'Segoe UI', 'Microsoft YaHei', 'Helvetica Neue', Arial, sans-serif;                        

        max-width: 1600px;                        video_image = gr.Image(

        margin: 0 auto;                            label="輸入圖像",

        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);                            type="filepath",

    }                            height=300

                            )

    .header-section {                        

        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);                        gr.Markdown("*上傳圖像或使用上一步生成的圖像*", elem_classes="professional-note")

        color: white;                        

        padding: 3rem 2rem;                        with gr.Row():

        border-radius: 15px;                            video_style = gr.Dropdown(

        text-align: center;                                choices=["smooth", "rotation", "zoom", "fade"],

        margin-bottom: 2rem;                                label="動畫風格", 

        box-shadow: 0 10px 30px rgba(0,0,0,0.15);                                value="smooth"

    }                            )

                                

    .header-section h1 {                            video_duration = gr.Slider(

        font-size: 3rem;                                minimum=2,

        font-weight: 300;                                maximum=10,

        margin: 0 0 1rem 0;                                value=4,

        text-shadow: 0 2px 4px rgba(0,0,0,0.1);                                step=1,

    }                                label="時長(秒)"

                                )

    .header-section p {                        

        font-size: 1.2rem;                        video_fps = gr.Slider(

        opacity: 0.95;                            minimum=15,

        margin: 0.5rem 0;                            maximum=30,

    }                            value=24,

                                step=1,

    .feature-panel {                            label="幀率(FPS)"

        background: white;                        )

        border-radius: 12px;                        

        padding: 2rem;                        video_btn = gr.Button("生成影片", variant="primary", size="lg")

        margin: 1.5rem 0;                    

        box-shadow: 0 4px 20px rgba(0,0,0,0.08);                    with gr.Column():

        border-left: 5px solid #667eea;                        gr.Markdown("### 生成結果", elem_classes="professional-header")

    }                        

                            video_output = gr.Video(

    .feature-panel h3 {                            label="AI生成的影片",

        color: #2c3e50;                            height=400

        font-weight: 600;                        )

        margin: 0 0 1rem 0;                        

        font-size: 1.3rem;                        video_status = gr.Textbox(

    }                            label="生成狀態",

                                lines=8, 

    .system-status {                            interactive=False

        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);                        )

        border-radius: 10px;            

        padding: 2rem;            # 系統信息標籤

        margin: 1rem 0;            with gr.Tab("系統信息"):

        border: 1px solid #dee2e6;                gr.HTML(f"""

    }                <div style="padding: 30px; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 12px; margin: 20px 0; border: 1px solid #dee2e6;">

                        <h3 style="color: #2c3e50; font-weight: 300; margin-bottom: 20px;">系統狀態</h3>

    .status-grid {                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 30px;">

        display: grid;                        <div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid #28a745;">

        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));                            <h4 style="margin: 0 0 10px 0; color: #28a745;">文案生成模組</h4>

        gap: 1rem;                            <p style="margin: 0; color: #6c757d;">高級模板系統 + AI增強技術</p>

        margin: 1.5rem 0;                        </div>

    }                        <div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid #007bff;">

                                <h4 style="margin: 0 0 10px 0; color: #007bff;">圖像生成模組</h4>

    .status-card {                            <p style="margin: 0; color: #6c757d;">Stable Diffusion XL (74GB模型)</p>

        background: white;                        </div>

        padding: 1.5rem;                        <div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid #6f42c1;">

        border-radius: 8px;                            <h4 style="margin: 0 0 10px 0; color: #6f42c1;">影片生成模組</h4>

        box-shadow: 0 2px 10px rgba(0,0,0,0.05);                            <p style="margin: 0; color: #6c757d;">OpenCV動畫處理引擎</p>

        border-left: 4px solid #28a745;                        </div>

    }                    </div>

                        

    .btn-primary {                    <h3 style="color: #2c3e50; font-weight: 300; margin-bottom: 20px;">核心功能</h3>

        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);                    <div style="background: white; padding: 25px; border-radius: 8px; margin-bottom: 30px;">

        border: none;                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">

        color: white;                            <div><strong>AI模型驅動</strong><br><span style="color: #6c757d;">使用業界領先的生成式AI技術</span></div>

        padding: 12px 30px;                            <div><strong>智能內容創作</strong><br><span style="color: #6c757d;">多風格模板系統，適應各種營銷需求</span></div>

        border-radius: 8px;                            <div><strong>專業級輸出</strong><br><span style="color: #6c757d;">高品質圖像和影片生成</span></div>

        font-weight: 500;                            <div><strong>自動化管理</strong><br><span style="color: #6c757d;">內容自動分類保存和版本控制</span></div>

        transition: all 0.3s ease;                        </div>

    }                    </div>

    """                    

                        <h3 style="color: #2c3e50; font-weight: 300; margin-bottom: 20px;">輸出管理</h3>

    with gr.Blocks(                    <div style="background: white; padding: 20px; border-radius: 8px; margin-bottom: 30px;">

        title="AI Marketing Professional Suite",                        <table style="width: 100%; border-collapse: collapse;">

        theme=gr.themes.Soft(),                            <tr style="border-bottom: 1px solid #dee2e6;">

        css=professional_css                                <td style="padding: 10px; font-weight: 500;">文案內容</td>

    ) as interface:                                <td style="padding: 10px; color: #6c757d;"><code>outputs/text/</code></td>

                                    </tr>

        # 專業標題區                            <tr style="border-bottom: 1px solid #dee2e6;">

        gr.HTML("""                                <td style="padding: 10px; font-weight: 500;">圖像文件</td>

        <div class="header-section">                                <td style="padding: 10px; color: #6c757d;"><code>outputs/images/</code></td>

            <h1>AI Marketing Professional Suite</h1>                            </tr>

            <p>Enterprise-Grade Content Generation Platform</p>                            <tr>

            <p>🚀 Text Generation • 🎨 AI Image Creation • 🎬 Video Production</p>                                <td style="padding: 10px; font-weight: 500;">影片文件</td>

            <p style="margin-top: 1.5rem; font-size: 1.1rem;"><strong>🌐 Public Access: http://140.119.235.6</strong></p>                                <td style="padding: 10px; color: #6c757d;"><code>outputs/videos/</code></td>

        </div>                            </tr>

        """)                        </table>

                            </div>

        # 主功能標籤頁                    

        with gr.Tabs():                    <h3 style="color: #2c3e50; font-weight: 300; margin-bottom: 20px;">使用指南</h3>

            # 內容創作標籤                    <div style="background: white; padding: 20px; border-radius: 8px;">

            with gr.Tab("📝 Smart Content Creation"):                        <p style="margin-bottom: 15px;"><strong>最佳實踐建議</strong></p>

                gr.HTML('<div class="feature-panel"><h3>AI-Powered Marketing Content Generation</h3><p>Create compelling marketing copy with advanced AI algorithms and professional templates.</p></div>')                        <ul style="color: #6c757d; line-height: 1.6;">

                                            <li>圖像提示詞建議在50字以內，使用關鍵詞組合</li>

                with gr.Row():                            <li>不同藝術風格適合不同類型的營銷內容</li>

                    with gr.Column(scale=1):                            <li>圖像生成需要1-3分鐘，影片生成相對較快</li>

                        gr.Markdown("### Content Parameters")                            <li>每次生成具有隨機性，可嘗試多次獲得最佳效果</li>

                                                    <li>建議使用GPU以獲得最佳性能表現</li>

                        product_input = gr.Textbox(                        </ul>

                            label="Product/Service Name",                    </div>

                            placeholder="Enter your product or service name",                </div>

                            value="Premium Smart Device"                """)

                        )        

                                # 綁定事件

                        style_input = gr.Dropdown(        text_btn.click(

                            label="Marketing Style",            fn=generate_text_advanced,

                            choices=["專業商務", "創新科技", "溫馨生活"],            inputs=[product_name, target_audience, content_type, tone, language],

                            value="專業商務",            outputs=[text_output, text_status],

                            info="Select the marketing approach that aligns with your brand"            show_progress=True

                        )        )

                                

                        audience_input = gr.Textbox(        image_btn.click(

                            label="Target Audience",            fn=generate_image_with_diffusers,

                            placeholder="Describe your target customers",            inputs=[image_prompt, image_style, image_size, image_quality],

                            value="Business professionals aged 25-45"            outputs=[image_output, image_status], 

                        )            show_progress=True

                                )

                        features_input = gr.Textbox(        

                            label="Key Features & Benefits",        video_btn.click(

                            placeholder="List your product's main selling points",            fn=generate_video_from_image,

                            lines=5,            inputs=[video_image, video_style, video_duration, video_fps],

                            value="Advanced technology\nUser-friendly interface\nHigh reliability\nExcellent support\nCompetitive pricing"            outputs=[video_output, video_status],

                        )            show_progress=True

                                )

                        tone_input = gr.Radio(        

                            label="Communication Style",        # 圖像自動傳遞到影片生成

                            choices=[("Professional & Formal", "formal"), ("Engaging & Persuasive", "persuasive")],        image_output.change(

                            value="formal"            fn=lambda x: x,

                        )            inputs=[image_output],

                                    outputs=[video_image]

                        content_generate_btn = gr.Button("Generate Professional Content", variant="primary", size="lg")        )

                        

                    with gr.Column(scale=2):    return demo

                        content_output = gr.Textbox(

                            label="Generated Marketing Content",if __name__ == "__main__":

                            lines=25,    print("\n" + "=" * 80)

                            show_copy_button=True,    print("AI MARKETING CONTENT GENERATION SYSTEM - PRODUCTION READY")

                            placeholder="Professional marketing content will appear here..."    print("=" * 80)

                        )    print("System Modules:")

                            print("  • Text Generation: Advanced Template Engine")

                        content_info_output = gr.Textbox(    print("  • Image Generation: Stable Diffusion XL AI Model") 

                            label="Generation Information",    print("  • Video Generation: Professional Animation Engine")

                            lines=4,    print("  • Content Management: Automated Output Organization")

                            interactive=False    print("=" * 80)

                        )    print("Starting Web Interface...")

                print("Access URL: http://localhost:7861")

            # 圖片創作標籤    print("=" * 80)

            with gr.Tab("🎨 Professional Image Generation"):    

                gr.HTML('<div class="feature-panel"><h3>AI-Powered Visual Content Creation</h3><p>Generate high-quality marketing images using state-of-the-art AI technology.</p></div>')    demo = create_complete_interface()

                    

                with gr.Row():    # 生產環境安全配置

                    with gr.Column(scale=1):    import os

                        gr.Markdown("### Image Specifications")    auth_config = None

                            

                        img_description_input = gr.Textbox(    # 如果設置了環境變量，啟用認證

                            label="Image Description",    if os.getenv("AI_MARKETING_USERNAME") and os.getenv("AI_MARKETING_PASSWORD"):

                            placeholder="Describe the image you want to create",        auth_config = (os.getenv("AI_MARKETING_USERNAME"), os.getenv("AI_MARKETING_PASSWORD"))

                            lines=4,        print("Security: User authentication enabled")

                            value="professional product photography of a sleek modern device on clean background with studio lighting"    

                        )    print("🌐 配置公網訪問模式...")

                            print("🔗 本地訪問: http://localhost:7861")

                        img_style_input = gr.Dropdown(    print("🔗 局域網訪問: http://[你的內網IP]:7861")

                            label="Visual Style Category",    print("🔗 公網訪問: http://[你的公網IP]:7861")

                            choices=["商業攝影", "創意設計", "品牌形象", "社交媒體", "印刷媒體"],    print("💡 提示: 需要在路由器/防火牆開放7861端口")

                            value="商業攝影"    print("=" * 80)

                        )    

                            demo.launch(

                        img_dimensions_input = gr.Dropdown(        server_name="0.0.0.0",  # 監聽所有網路接口

                            label="Image Dimensions",        server_port=int(os.getenv("PORT", 7861)),

                            choices=["1024x1024", "1024x768", "768x1024", "1280x720", "1920x1080"],        share=False,  # 關閉Gradio分享，直接公網部署

                            value="1024x1024"        show_error=False,

                        )        quiet=False,

                                inbrowser=False,

                        img_quality_input = gr.Slider(        auth=auth_config

                            label="Generation Quality",    )
                            minimum=20,
                            maximum=50,
                            value=35,
                            step=5,
                            info="Higher values produce better quality"
                        )
                        
                        img_guidance_input = gr.Slider(
                            label="Prompt Adherence",
                            minimum=5.0,
                            maximum=15.0,
                            value=8.0,
                            step=0.5,
                            info="How closely to follow the description"
                        )
                        
                        image_generate_btn = gr.Button("Generate Professional Image", variant="primary", size="lg")
                    
                    with gr.Column(scale=2):
                        image_output = gr.Image(
                            label="Generated Professional Image",
                            height=600,
                            show_download_button=True
                        )
                        
                        image_info_output = gr.Textbox(
                            label="Generation Details",
                            lines=5,
                            interactive=False
                        )
            
            # 影片製作標籤
            with gr.Tab("🎬 Video Production Studio"):
                gr.HTML('<div class="feature-panel"><h3>Dynamic Marketing Video Creation</h3><p>Produce engaging marketing videos with professional animations and effects.</p></div>')
                
                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown("### Video Specifications")
                        
                        video_title_input = gr.Textbox(
                            label="Product/Brand Title",
                            placeholder="Title to feature in the video",
                            value="Premium Smart Device"
                        )
                        
                        video_category_input = gr.Dropdown(
                            label="Video Category",
                            choices=["產品展示", "品牌動畫", "促銷廣告"],
                            value="產品展示",
                            info="Choose the video style for your campaign"
                        )
                        
                        video_duration_input = gr.Slider(
                            label="Video Duration (seconds)",
                            minimum=5,
                            maximum=30,
                            value=15,
                            step=5,
                            info="Optimal length for social media: 10-15 seconds"
                        )
                        
                        video_resolution_input = gr.Dropdown(
                            label="Video Resolution",
                            choices=["1920x1080", "1280x720", "1024x1024"],
                            value="1280x720",
                            info="Choose resolution based on platform requirements"
                        )
                        
                        video_generate_btn = gr.Button("Generate Marketing Video", variant="primary", size="lg")
                    
                    with gr.Column(scale=2):
                        video_output = gr.Video(
                            label="Generated Marketing Video",
                            height=500
                        )
                        
                        video_info_output = gr.Textbox(
                            label="Production Details",
                            lines=5,
                            interactive=False
                        )
            
            # 系統狀態標籤
            with gr.Tab("ℹ️ System Dashboard"):
                gr.HTML(f"""
                <div class="system-status">
                    <h3 style="color: #2c3e50; margin-bottom: 1.5rem;">System Status Dashboard</h3>
                    
                    <div class="status-grid">
                        <div class="status-card">
                            <h4 style="margin: 0 0 0.5rem 0; color: #28a745;">🤖 AI Models</h4>
                            <p style="margin: 0; color: #6c757d;">Stable Diffusion XL + Custom Engines</p>
                        </div>
                        
                        <div class="status-card">
                            <h4 style="margin: 0 0 0.5rem 0; color: #007bff;">💻 Processing</h4>
                            <p style="margin: 0; color: #6c757d;">{ai_system.device.upper()} Acceleration</p>
                        </div>
                        
                        <div class="status-card">
                            <h4 style="margin: 0 0 0.5rem 0; color: #ffc107;">🚀 Status</h4>
                            <p style="margin: 0; color: #6c757d;">✅ All Systems Operational</p>
                        </div>
                    </div>
                    
                    <h4 style="color: #2c3e50; margin: 2rem 0 1rem 0;">Access Information</h4>
                    <table style="width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden;">
                        <tr style="background: #f8f9fa;">
                            <td style="padding: 1rem; font-weight: 600; border-bottom: 1px solid #dee2e6;">Access Type</td>
                            <td style="padding: 1rem; font-weight: 600; border-bottom: 1px solid #dee2e6;">URL</td>
                        </tr>
                        <tr>
                            <td style="padding: 1rem; border-bottom: 1px solid #dee2e6;">🌐 Public Access</td>
                            <td style="padding: 1rem; border-bottom: 1px solid #dee2e6;"><code>http://140.119.235.6</code></td>
                        </tr>
                        <tr>
                            <td style="padding: 1rem;">🏠 Local Access</td>
                            <td style="padding: 1rem;"><code>http://localhost</code></td>
                        </tr>
                    </table>
                    
                    <h4 style="color: #2c3e50; margin: 2rem 0 1rem 0;">Platform Capabilities</h4>
                    <div style="background: white; padding: 1.5rem; border-radius: 8px; line-height: 1.6;">
                        <ul style="margin: 0; padding-left: 1.5rem;">
                            <li><strong>Content Generation:</strong> Professional marketing copy with multiple styles and tones</li>
                            <li><strong>Image Creation:</strong> High-quality AI-generated visuals using Stable Diffusion XL</li>
                            <li><strong>Video Production:</strong> Dynamic marketing videos with custom animations</li>
                            <li><strong>Style Variety:</strong> Business, Technology, and Lifestyle themes</li>
                            <li><strong>Quality Control:</strong> Adjustable parameters for optimal output</li>
                            <li><strong>File Management:</strong> Automatic saving with organized folder structure</li>
                        </ul>
                    </div>
                </div>
                """)
        
        # 綁定所有功能
        content_generate_btn.click(
            fn=ai_system.generate_professional_content,
            inputs=[product_input, style_input, audience_input, features_input, tone_input],
            outputs=[content_output, content_info_output]
        )
        
        image_generate_btn.click(
            fn=ai_system.create_professional_image,
            inputs=[img_description_input, img_style_input, img_dimensions_input, img_quality_input, img_guidance_input],
            outputs=[image_output, image_info_output]
        )
        
        video_generate_btn.click(
            fn=ai_system.create_marketing_video,
            inputs=[video_title_input, video_category_input, video_duration_input, video_resolution_input],
            outputs=[video_output, video_info_output]
        )
    
    return interface

if __name__ == "__main__":
    print("=" * 90)
    print("🚀 AI MARKETING PROFESSIONAL SUITE - ENTERPRISE EDITION")
    print("=" * 90)
    print("🎯 Complete Solution: Advanced Text + Image + Video Generation")
    print("🤖 AI Technology: Stable Diffusion XL + Custom Animation Engine")
    print("🌐 Public Access: http://140.119.235.6")
    print(f"⚙️ Processing Mode: {'GPU Accelerated' if torch.cuda.is_available() else 'CPU Optimized'}")
    print("📁 Content Management: Auto-save with organized folder structure")
    print("🔧 Quality Assurance: Professional-grade output with adjustable parameters")
    print("=" * 90)
    
    # 創建並啟動專業界面
    professional_interface = create_complete_professional_interface()
    
    # 智能端口選擇
    available_ports = [80, 8080, 7861, 3000, 5000, 8000]
    
    for port_number in available_ports:
        try:
            access_url = f"http://140.119.235.6:{port_number}" if port_number != 80 else "http://140.119.235.6"
            
            print(f"\n🔗 Starting server on port {port_number}...")
            print(f"🌐 Public URL: {access_url}")
            print(f"🏠 Local URL: http://localhost:{port_number if port_number != 80 else ''}")
            
            professional_interface.launch(
                server_name="0.0.0.0",
                server_port=port_number,
                share=False,
                show_error=True,
                quiet=False,
                inbrowser=False
            )
            
            print(f"✅ Successfully launched on port {port_number}")
            break
            
        except PermissionError:
            print(f"⚠️ Port {port_number} requires administrator privileges")
            continue
        except OSError as os_error:
            if "address already in use" in str(os_error).lower():
                print(f"⚠️ Port {port_number} is already in use")
            continue
        except Exception as launch_error:
            print(f"❌ Failed to launch on port {port_number}: {launch_error}")
            continue
    else:
        print("\n❌ Unable to start server on any available port")
        print("💡 Please check system status and try again")