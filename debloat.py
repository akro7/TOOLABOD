import os
import shutil
import threading
import glob
import customtkinter as ctk
from tkinter import filedialog, messagebox
from concurrent.futures import ThreadPoolExecutor

# UI Configuration
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class AhmedYounisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("QUANTUM DEBLOATER PRO | ELITE EDITION")
        self.root.geometry("700x550")
        
        # Developer Data
        self.developer = "Ahmed Younis"
        self.co_developer = "ABOD"
        self.version = "3.1.0"
        
        # Counters
        self.deleted_count = 0
        self.lock = threading.Lock()

        # Full App List mapped from Bash Script
        self.debloat_apps = [
            "SpeechServicesByGoogle", "HMT", "PaymentFramework", "SamsungCalendar", "LiveTranscribe",
            "DigitalWellbeing", "Maps", "Duo", "Photos", "FactoryCameraFB", "WlanTest", "AssistantShell",
            "BardShell", "DuoStub", "GoogleCalendarSyncAdapter", "AndroidDeveloperVerifier", "AndroidGlassesCore",
            "SOAgent77", "YourPhone_Stub", "AndroidAutoStub", "SingleTakeService", "SamsungBilling",
            "AndroidSystemIntelligence", "GoogleRestore", "Messages", "SearchSelector", "AirGlance",
            "AirReadingGlass", "SamsungTTS", "WlanTest", "ARCore", "ARDrawing", "ARZone", "BGMProvider", "BixbyWakeup",
            "BlockchainBasicKit", "Cameralyzer", "DictDiotekForSec", "EasymodeContactsWidget81", "Fast",
            "FBAppManager_NS", "FunModeSDK", "GearManagerStub", "KidsHome_Installer", "LinkSharing_v11",
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
            "SamsungPass", "SamsungSmartSuggestions", "SettingsBixby", "SetupIndiaServicesTnC", "SKTFindLostPhone",
            "SKTHiddenMenu", "SKTMemberShip", "SKTOneStore", "SktUsimService", "SmartEye", "SmartPush", "SmartThingsKit",
            "SmartTouchCall", "SOAgent7", "SOAgent75", "SolarAudio-service", "SPPPushClient", "sticker",
            "StickerFaceARAvatar", "StoryService", "SumeNNService", "SVoiceIME", "SwiftkeyIme",
            "SwiftkeySetting", "SystemUpdate", "TADownloader", "TalkbackSE", "TaPackAuthFw", "TPhoneOnePackage",
            "TPhoneSetup", "TWorld", "UltraDataSaving_O", "Upday", "UsimRegistrationKOR", "YourPhone_P1_5", "AvatarPicker",
            "GpuWatchApp", "KT114Provider2", "KTHiddenMenu", "KTOneStore", "KTServiceAgent", "KTServiceMenu",
            "LGUGPSnWPS", "LGUHiddenMenu", "LGUOZStore", "SKTFindLostPhoneApp", "SmartPush_64", "SOAgent76",
            "TService", "vexfwk_service", "VexScanner", "LiveEffectService", "YourPhone_P1_5", "vexfwk_service"
        ]

        self.setup_ui()

    def setup_ui(self):
        # Main Title
        self.lbl_title = ctk.CTkLabel(self.root, text="QUANTUM DEBLOATER", font=("Orbitron", 28, "bold"), text_color="#00D4FF")
        self.lbl_title.pack(pady=20)

        # Path Frame
        self.path_frame = ctk.CTkFrame(self.root)
        self.path_frame.pack(pady=10, padx=20, fill="x")

        self.entry_path = ctk.CTkEntry(self.path_frame, placeholder_text="Extracted Firmware Path...", width=400)
        self.entry_path.pack(side="left", padx=10, pady=10, expand=True, fill="x")

        self.btn_browse = ctk.CTkButton(self.path_frame, text="BROWSE", command=self.browse_path, width=100, fg_color="#FFD700", text_color="black")
        self.btn_browse.pack(side="right", padx=10)

        # Log Area
        self.txt_log = ctk.CTkTextbox(self.root, width=600, height=200, state="disabled", font=("Consolas", 12))
        self.txt_log.pack(pady=20, padx=20)

        # Progress Bar
        self.progress = ctk.CTkProgressBar(self.root, width=600)
        self.progress.set(0)
        self.progress.pack(pady=10)

        # Start Button
        self.btn_start = ctk.CTkButton(self.root, text="START OPTIMIZATION", command=self.start_process, font=("bold", 16), height=45, fg_color="#1A5F7A")
        self.btn_start.pack(pady=20)

        # Credits Footer
        self.lbl_credits = ctk.CTkLabel(self.root, text=f"Lead Developer: {self.developer} | Co-Developer: {self.co_developer} | v{self.version}", font=("Arial", 10))
        self.lbl_credits.pack(side="bottom", pady=5)

    def browse_path(self):
        path = filedialog.askdirectory()
        if path:
            self.entry_path.delete(0, "end")
            self.entry_path.insert(0, path)

    def log(self, message):
        self.txt_log.configure(state="normal")
        self.txt_log.insert("end", f"> {message}\n")
        self.txt_log.see("end")
        self.txt_log.configure(state="disabled")

    def secure_delete(self, path):
        if os.path.exists(path):
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
                with self.lock:
                    self.deleted_count += 1
                return True
            except:
                pass
        return False

    def resolve_wildcards(self, target_dir, paths):
        resolved = []
        for p in paths:
            full_path = os.path.join(target_dir, p)
            if "*" in full_path:
                resolved.extend(glob.glob(full_path))
            else:
                resolved.append(full_path)
        return resolved

    def start_process(self):
        target = self.entry_path.get()
        if not target or not os.path.exists(target):
            messagebox.showerror("Error", "Please select a valid firmware path!")
            return
        
        self.btn_start.configure(state="disabled")
        self.deleted_count = 0
        self.log("Starting Elite Optimization...")
        threading.Thread(target=self.debloat_logic, args=(target,), daemon=True).start()

    def debloat_logic(self, target_dir):
        targets = []
        
        # 1. App Kick List
        app_sub_dirs = ["system/system/app", "system/system/priv-app", "product/app", "product/priv-app"]
        for app in self.debloat_apps:
            for sub_dir in app_sub_dirs:
                targets.append(os.path.join(target_dir, sub_dir, app))
        
        # 2. eSIM Files Mapping
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
        
        # 3. Fabric Crypto Mapping
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
        
        # 4. Extra Cleanup & Wildcards Mapping
        extra_paths = [
            "system/system/app/SamsungTTS*",
            "system/system/etc/init/boot-image.bprof",
            "system/system/etc/init/boot-image.prof",
            "system/system/etc/mediasearch",
            "system/system/hidden",
            "system/system/preload",
            "system/system/priv-app/MediaSearch",
            "system/system/priv-app/GameDriver-*",
            "system/system/tts",
            "product/app/Gmail2/oat",
            "product/app/Maps/oat",
            "product/app/SpeechServicesByGoogle/oat",
            "product/app/YouTube/oat",
            "product/priv-app/HotwordEnrollment*"
        ]

        # Combine all and resolve wildcards (*)
        all_raw_paths = esim_paths + fabric_paths + extra_paths
        resolved_paths = self.resolve_wildcards(target_dir, all_raw_paths)
        targets.extend(resolved_paths)

        # Execute Deletion
        total = len(targets)
        if total == 0:
            self.log("No targets found to clean.")
            self.btn_start.configure(state="normal")
            return

        with ThreadPoolExecutor(max_workers=20) as executor:
            for i, _ in enumerate(executor.map(self.secure_delete, targets)):
                self.progress.set((i + 1) / total)
                if i % 10 == 0 or i == total - 1:
                    self.log(f"Processing item {i+1} of {total}...")

        self.log(f"Optimization Complete! Purged {self.deleted_count} items.")
        self.btn_start.configure(state="normal")
        messagebox.showinfo("Quantum Pro", f"Optimization Complete!\nItems Removed: {self.deleted_count}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = AhmedYounisGUI(root)
    root.mainloop()
