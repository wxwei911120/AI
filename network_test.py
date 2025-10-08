#!/usr/bin/env python3
"""
網絡連接測試工具
測試公網IP可訪問性
"""

import requests
import socket
import time

def test_local_connection():
    """測試本地連接"""
    try:
        response = requests.get("http://localhost:80", timeout=5)
        print(f"✅ 本地連接成功: HTTP {response.status_code}")
        return True
    except Exception as e:
        print(f"❌ 本地連接失敗: {e}")
        return False

def test_network_interface():
    """測試網絡界面"""
    try:
        response = requests.get("http://0.0.0.0:80", timeout=5)
        print(f"✅ 網絡界面連接成功: HTTP {response.status_code}")
        return True
    except Exception as e:
        print(f"❌ 網絡界面連接失敗: {e}")
        return False

def test_public_ip():
    """測試公網IP"""
    try:
        response = requests.get("http://140.119.235.6:80", timeout=10)
        print(f"✅ 公網IP連接成功: HTTP {response.status_code}")
        return True
    except Exception as e:
        print(f"❌ 公網IP連接失敗: {e}")
        return False

def check_port_listening():
    """檢查端口監聽狀況"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 80))
        sock.close()
        if result == 0:
            print("✅ 端口80正在監聽")
            return True
        else:
            print("❌ 端口80未監聽")
            return False
    except Exception as e:
        print(f"❌ 端口檢查失敗: {e}")
        return False

def main():
    print("=" * 60)
    print("🔍 AI營銷系統網絡連接測試")
    print("=" * 60)
    
    print("\n1️⃣ 檢查端口監聽狀況:")
    port_ok = check_port_listening()
    
    print("\n2️⃣ 測試本地連接:")
    local_ok = test_local_connection()
    
    print("\n3️⃣ 測試網絡界面連接:")
    interface_ok = test_network_interface()
    
    print("\n4️⃣ 測試公網IP連接:")
    public_ok = test_public_ip()
    
    print("\n" + "=" * 60)
    print("📊 測試結果總結:")
    print(f"   端口監聽: {'✅' if port_ok else '❌'}")
    print(f"   本地連接: {'✅' if local_ok else '❌'}")
    print(f"   網絡界面: {'✅' if interface_ok else '❌'}")
    print(f"   公網訪問: {'✅' if public_ok else '❌'}")
    
    if all([port_ok, local_ok, interface_ok, public_ok]):
        print("\n🎉 所有測試通過！系統可公網訪問")
        print("🌐 訪問地址: http://140.119.235.6")
    else:
        print("\n⚠️ 部分測試失敗，需要進一步配置")
        if not port_ok:
            print("💡 建議: 檢查服務是否正常啟動")
        if not public_ok:
            print("💡 建議: 檢查防火牆和路由配置")
    
    print("=" * 60)

if __name__ == "__main__":
    main()