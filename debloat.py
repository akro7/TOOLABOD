import os
import sys
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk

# دالة التعامل مع الملفات المدمجة داخل الـ EXE (مثل ADB و Fastboot)
def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class DebloaterTool(ctk.CTk):
    def __init__(self):
        super().__init__()

        # إعدادات الواجهة (Advanced Cyber-UI)
        self.title("QuantumROM Debloater Tool - Windows Edition")
        self.geometry("800x650")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # القائمة الكاملة والنهائية المنسوخة حرفياً من سكريبت الـ Bash الخاص بك
        self.DEBLOAT_APPS = [
            "SpeechServicesByGoogle", "HMT", "PaymentFramework", "SamsungCalendar", "LiveTranscribe", 
            "DigitalWellbeing", "Maps", "Duo", "Photos", "FactoryCameraFB", "WlanTest", "AssistantShell", 
            "BardShell", "DuoStub", "GoogleCalendarSyncAdapter", "AndroidDeveloperVerifier", 
            "AndroidGlassesCore", "SOAgent77", "YourPhone_Stub", "AndroidAutoStub", "SingleTakeService", 
            "SamsungBilling", "AndroidSystemIntelligence", "GoogleRestore", "Messages", "SearchSelector", 
            "AirGlance", "AirReadingGlass", "SamsungTTS", "ARCore", "ARDrawing", "ARZone", "BGMProvider", 
            "BixbyWakeup", "BlockchainBasicKit", "Cameralyzer", "DictDiotekForSec", "EasymodeContactsWidget81", 
            "Fast", "FBAppManager_NS", "FunModeSDK", "GearManagerStub", "KidsHome_Installer", "LinkSharing_v11", 
            "LiveDrawing", "MAPSAgent", "MdecService", "MinusOnePage", "MoccaMobile", "Netflix_stub", "Notes40", 
            "ParentalCare", "PhotoTable", "PlayAutoInstallConfig", "SamsungPassAutofill_v1", "SmartReminder", 
            "SmartSwitchStub", "UnifiedWFC", "UniversalMDMClient", "VideoEditorLite_Dream_N", "VisionIntelligence3.7", 
            "VoiceAccess", "VTCameraSetting", "WebManual", "WifiGuider", "KTAuth", "KTCustomerService", 
            "KTUsimManager", "LGUMiniCustomerCenter", "LGUplusTsmProxy", "SketchBook", "SKTMemberShip_new", 
            "SktUsimService", "TWorld", "AirCommand", "AppUpdateCenter", "AREmoji", "AREmojiEditor", 
            "AuthFramework", "AutoDoodle", "AvatarEmojiSticker", "AvatarEmojiSticker_S", "Bixby", 
            "BixbyInterpreter", "BixbyVisionFramework3.5", "DevGPUDriver-EX2200", "DigitalKey", "Discover", 
            "DiscoverSEP", "EarphoneTypeC", "EasySetup", "FBInstaller_NS", "FBServices", "FotaAgent", 
            "GalleryWidget", "GameDriver-EX2100", "GameDriver-EX2200", "GameDriver-SM8150", "HashTagService", 
            "MultiControlVP6", "LedCoverService", "LinkToWindowsService", "LiveStickers", "MemorySaver_O_Refresh", 
            "MultiControl", "OMCAgent5", "OneDrive_Samsung_v3", "OneStoreService", "SamsungCarKeyFw", 
            "SamsungPass", "SamsungSmartSuggestions", "SettingsBixby", "SetupIndiaServicesTnC", 
            "SKTFindLostPhone", "SKTHiddenMenu", "SKTMemberShip", "SKTOneStore", "SmartEye", "SmartPush", 
            "SmartThingsKit", "SmartTouchCall", "SOAgent7", "SOAgent75", "SolarAudio-service", "SPPPushClient", 
            "sticker", "StickerFaceARAvatar", "StoryService", "SumeNNService", "SVoiceIME", "SwiftkeyIme", 
            "SwiftkeySetting", "SystemUpdate", "TADownloader", "TalkbackSE", "TaPackAuthFw", "TPhoneOnePackage", 
            "TPhoneSetup", "UltraDataSaving_O", "Upday", "UsimRegistrationKOR", "YourPhone_P1_5", "AvatarPicker", 
            "GpuWatchApp", "KT114Provider2", "KTHiddenMenu", "KTOneStore", "KTServiceAgent", "KTServiceMenu", 
            "LGUGPSnWPS", "LGUHiddenMenu", "LGUOZStore", "SKTFindLostPhoneApp", "SmartPush_64", "SOAgent76", 
            "TService", "vexfwk_service", "VexScanner", "LiveEffectService"
        ]

        # UI Elements
        self.label = ctk.CTkLabel(self, text="QUANTUM DEBLOAT ENGINE", font=("Orbitron", 28, "bold"), text_color="#00D4FF")
        self.label.pack(pady=20)

        self.path_frame = ctk.CTkFrame(self)
        self.path_frame.pack(pady=10, padx=20, fill="x")

        self.path_entry = ctk.CTkEntry(self.path_frame, width=500, placeholder_text="Target Path: (e.g. C:/Quantum/extracted_firmware)")
        self.path_entry.pack(side="left", padx=10, pady=10)

        self.browse_btn = ctk.CTkButton(self.path_frame, text="BROWSE", width=100, command=self.browse_folder)
        self.browse_btn.pack(side="left", padx=5)

        # الخيارات المتقدمة (Advanced Control)
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.pack(pady=10, padx=20, fill="x")

        self.kick_var = ctk.BooleanVar(value=True)
        self.kick_check = ctk.CTkCheckBox(self.options_frame, text="Execute KICK() Logic (Deep Bloatware Strip)", variable=self.kick_var)
        self.kick_check.pack(pady=5, padx=20, anchor="w")

        self.esim_var = ctk.BooleanVar(value=False)
        self.esim_check = ctk.CTkCheckBox(self.options_frame, text="Wipe eSIM Telephony Modules (eSIM Purge)", variable=self.esim_var, text_color="#E74C3C")
        self.esim_check.pack(pady=5, padx=20, anchor="w")

        self.fabric_var = ctk.BooleanVar(value=True)
        self.fabric_check = ctk.CTkCheckBox(self.options_frame, text="Eradicate Fabric Crypto & Knox Services", variable=self.fabric_var)
        self.fabric_check.pack(pady=5, padx=20, anchor="w")

        self.junk_var = ctk.BooleanVar(value=True)
        self.junk_check = ctk.CTkCheckBox(self.options_frame, text="Purge Residual Junk (TTS, Preloads, OAT Logs)", variable=self.junk_var)
        self.junk_check.pack(pady=5, padx=20, anchor="w")

        # Console Log
        self.log_text = ctk.CTkTextbox(self, width=750, height=220, font=("Consolas", 12))
        self.log_text.pack(pady=15, padx=20)

        # Start Button
        self.start_btn = ctk.CTkButton(self, text="INITIALIZE DEBLOAT STAGE", height=50, font=("Arial", 18, "bold"), 
                                        fg_color="#1F618D", hover_color="#2E86C1", command=self.start_debloat)
        self.start_btn.pack(pady=10)

        # Developer Credit
        self.footer = ctk.CTkLabel(self, text="LEAD DEVELOPER: AHMED YOUNIS (AKRO)", font=("Arial", 11, "bold"), text_color="#5D6D7E")
        self.footer.pack(side="bottom", pady=5)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder_selected)

    def log(self, message):
        self.log_text.insert(tk.END, f"[#] {message}\n")
        self.log_text.see(tk.END)
        self.update_idletasks()

    def start_debloat(self):
        base_path = self.path_entry.get().strip()
        if not base_path or not os.path.exists(base_path):
            messagebox.showerror("IO_ERROR", "Target directory not found. Please select a valid path.")
            return

        self.log_text.delete("1.0", tk.END)
        self.log("BOOTING QUANTUM ENGINE...")

        # 1. نظام الـ KICK() - حذف التطبيقات
        if self.kick_var.get():
            self.log("EXECUTING KICK SEQUENCE...")
            app_partitions = [
                "system/system/app", "system/system/priv-app", 
                "product/app", "product/priv-app"
            ]
            for app in self.DEBLOAT_APPS:
                for part in app_partitions:
                    target = os.path.join(base_path, part, app)
                    if os.path.exists(target):
                        try:
                            shutil.rmtree(target)
                            self.log(f"STRIPPED: {app}")
                        except: pass

        # 2. نظام الـ eSIM Removal
        if self.esim_var.get():
            self.log("PURGING ESIM TELEPHONY DATA...")
            self.remove_esim_logic(base_path)

        # 3. نظام الـ Fabric Crypto
        if self.fabric_var.get():
            self.log("ERADICATING FABRIC CRYPTO DEPS...")
            self.remove_fabric_logic(base_path)

        # 4. نظام الـ Junk & Unnecessary (اللمسات النهائية من السكريبت)
        if self.junk_var.get():
            self.log("CLEANING RESIDUAL STAGING FILES...")
            self.clean_extra_junk(base_path)

        self.log("-----------------------------------------")
        self.log("OPERATION SUCCESSFUL: SYSTEM OPTIMIZED.")
        messagebox.showinfo("QUANTUM_DONE", "Debloat process completed successfully.")

    def remove_esim_logic(self, base_path):
        esim_paths = [
            "system/system/etc/autoinstalls/autoinstalls-com.google.android.euicc",
            "system/system/etc/default-permissions/default-permissions-com.google.android.euicc.xml",
            "system/system/etc/permissions/privapp-permissions-com.samsung.euicc.xml",
            "system/system/etc/permissions/privapp-permissions-com.samsung.android.app.esimkeystring.xml",
            "system/system/etc/permissions/privapp-permissions-com.samsung.android.app.telephonyui.esimclient.xml",
            "system/system/etc/privapp-permissions-com.samsung.android.app.telephonyui.esimclient.xml",
            "system/system/etc/sysconfig/preinstalled-packages-com.samsung.euicc.xml",
            "system/system/etc/sysconfig/preinstalled-packages-com.samsung.android.app.esimkeystring.xml",
            "system/system/priv-app/EsimClient",
            "system/system/priv-app/EsimKeyString",
            "system/system/priv-app/EuiccService",
            "system/system/priv-app/EuiccGoogle"
        ]
        for p in esim_paths:
            full = os.path.join(base_path, p)
            if os.path.exists(full):
                if os.path.isdir(full): shutil.rmtree(full)
                else: os.remove(full)
                self.log(f"REMOVED_ESIM: {os.path.basename(p)}")

    def remove_fabric_logic(self, base_path):
        fabric_paths = [
            "system/system/bin/fabric_crypto",
            "system/system/etc/init/fabric_crypto.rc",
            "system/system/etc/permissions/FabricCryptoLib.xml",
            "system/system/etc/vintf/manifest/fabric_crypto_manifest.xml",
            "system/system/framework/FabricCryptoLib.jar",
            "system/system/framework/oat/arm/FabricCryptoLib.odex",
            "system/system/framework/oat/arm/FabricCryptoLib.vdex",
            "system/system/framework/oat/arm64/FabricCryptoLib.odex",
            "system/system/framework/oat/arm64/FabricCryptoLib.vdex",
            "system/system/lib64/com.samsung.security.fabric.cryptod-V1-cpp.so",
            "system/system/lib64/vendor.samsung.hardware.security.fkeymaster-V1-ndk.so",
            "system/system/priv-app/KmxService"
        ]
        for f in fabric_paths:
            full = os.path.join(base_path, f)
            if os.path.exists(full):
                if os.path.isdir(full): shutil.rmtree(full)
                else: os.remove(full)
                self.log(f"WIPED_FABRIC: {os.path.basename(f)}")

    def clean_extra_junk(self, base_path):
        # تنفيذ المسح العشوائي المذكور في نهاية وظيفة DEBLOAT()
        extra_junk = [
            "system/system/etc/init/boot-image.bprof",
            "system/system/etc/init/boot-image.prof",
            "system/system/etc/mediasearch",
            "system/system/hidden",
            "system/system/preload",
            "system/system/priv-app/MediaSearch",
            "system/system/tts",
            "product/app/Gmail2/oat",
            "product/app/Maps/oat",
            "product/app/SpeechServicesByGoogle/oat",
            "product/app/YouTube/oat"
        ]
        for j in extra_junk:
            full = os.path.join(base_path, j)
            if os.path.exists(full):
                if os.path.isdir(full): shutil.rmtree(full)
                else: os.remove(full)
                self.log(f"JUNK_PURGED: {j}")
        
        # التعامل مع Wildcards (SamsungTTS* و GameDriver-*)
        try:
            # مثال لـ SamsungTTS
            tts_dir = os.path.join(base_path, "system/system/app")
            if os.path.exists(tts_dir):
                for item in os.listdir(tts_dir):
                    if item.startswith("SamsungTTS"):
                        shutil.rmtree(os.path.join(tts_dir, item))
            
            # مثال لـ GameDriver
            gd_dir = os.path.join(base_path, "system/system/priv-app")
            if os.path.exists(gd_dir):
                for item in os.listdir(gd_dir):
                    if item.startswith("GameDriver-"):
                        shutil.rmtree(os.path.join(gd_dir, item))
        except: pass

if __name__ == "__main__":
    app = DebloaterTool()
    app.mainloop()
