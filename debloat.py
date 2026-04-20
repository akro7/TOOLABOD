import os
import shutil
import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

# تهيئة الألوان
init(autoreset=True)

class AhmedYounisDebloater:
    def __init__(self):
        self.developer = "Ahmed Younis"
        self.version = "3.1.0-Elite"
        self.target_dir = ""
        self.deleted_count = 0
        self.failed_count = 0
        self.lock = threading.Lock() # لضمان سلامة العدادات مع الـ Threads
        
        # قائمة تطبيقات عبود
        self.debloat_apps = [
            "SpeechServicesByGoogle", "HMT", "PaymentFramework", "SamsungCalendar", "LiveTranscribe",
            "DigitalWellbeing", "Maps", "Duo", "Photos", "FactoryCameraFB", "WlanTest", "AssistantShell",
            "BardShell", "DuoStub", "GoogleCalendarSyncAdapter", "AndroidDeveloperVerifier", "AndroidGlassesCore",
            "SOAgent77", "YourPhone_Stub", "AndroidAutoStub", "SingleTakeService", "SamsungBilling",
            "AndroidSystemIntelligence", "GoogleRestore", "Messages", "SearchSelector", "AirGlance",
            "AirReadingGlass", "SamsungTTS", "ARCore", "ARDrawing", "ARZone", "BGMProvider", "BixbyWakeup",
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
            "SKTHiddenMenu", "SKTMemberShip", "SKTOneStore", "SmartEye", "SmartPush", "SmartThingsKit",
            "SmartTouchCall", "SOAgent7", "SOAgent75", "SolarAudio-service", "SPPPushClient", "sticker",
            "StickerFaceARAvatar", "StoryService", "SumeNNService", "SVoiceIME", "SwiftkeyIme",
            "SwiftkeySetting", "SystemUpdate", "TADownloader", "TalkbackSE", "TaPackAuthFw", "TPhoneOnePackage",
            "TPhoneSetup", "UltraDataSaving_O", "Upday", "UsimRegistrationKOR", "YourPhone_P1_5", "AvatarPicker",
            "GpuWatchApp", "KT114Provider2", "KTHiddenMenu", "KTOneStore", "KTServiceAgent", "KTServiceMenu",
            "LGUGPSnWPS", "LGUHiddenMenu", "LGUOZStore", "SKTFindLostPhoneApp", "SmartPush_64", "SOAgent76",
            "TService", "vexfwk_service", "VexScanner", "LiveEffectService"
        ]

    def banner(self):
        # منع الخطأ إذا كان يعمل بدون Console
        if sys.stdout and sys.stdout.isatty():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{Fore.CYAN}{'='*60}")
            print(f"{Fore.YELLOW}   █████╗ ██╗  ██╗███╗   ███╗███████╗██████╗ ")
            print(f"{Fore.YELLOW}  ██╔══██╗██║  ██║████╗ ████║██╔════╝██╔══██╗")
            print(f"{Fore.YELLOW}  ███████║███████║██╔████╔██║█████╗  ██║  ██║")
            print(f"{Fore.YELLOW}  ██╔══██║██╔══██║██║╚██╔╝██║██╔══╝  ██║  ██║")
            print(f"{Fore.YELLOW}  ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗██████╔╝")
            print(f"{Fore.CYAN}{'='*60}")
            print(f"{Fore.GREEN}  >> DEVELOPED BY: {self.developer}")
            print(f"{Fore.MAGENTA}  >> VERSION: {self.version}")
            print(f"{Fore.CYAN}{'='*60}\n")

    def animate_loading(self, text):
        if sys.stdout and sys.stdout.isatty():
            chars = "/—\\|"
            for char in chars:
                sys.stdout.write(f'\r{Fore.BLUE}[{char}] {text}...')
                sys.stdout.flush()
                time.sleep(0.1)

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
                with self.lock:
                    self.failed_count += 1
        return False

    def remove_esim_files(self):
        self.animate_loading("Removing eSIM Infrastructure")
        paths = [
            "system/system/etc/autoinstalls/autoinstalls-com.google.android.euicc",
            "system/system/etc/default-permissions/default-permissions-com.google.android.euicc.xml",
            "system/system/etc/permissions/privapp-permissions-com.samsung.euicc.xml",
            "system/system/etc/permissions/privapp-permissions-com.samsung.android.app.esimkeystring.xml",
            "system/system/etc/permissions/privapp-permissions-com.samsung.android.app.telephonyui.esimclient.xml",
            "system/system/priv-app/EsimClient",
            "system/system/priv-app/EsimKeyString",
            "system/system/priv-app/EuiccService",
            "system/system/priv-app/EuiccGoogle"
        ]
        for p in paths:
            self.secure_delete(os.path.join(self.target_dir, p))
        if sys.stdout and sys.stdout.isatty(): print(f"\n{Fore.GREEN}[+] eSIM files purged.")

    def remove_fabric_crypto(self):
        self.animate_loading("Disabling Fabric Crypto")
        paths = [
            "system/system/bin/fabric_crypto",
            "system/system/etc/init/fabric_crypto.rc",
            "system/system/etc/permissions/FabricCryptoLib.xml",
            "system/system/framework/FabricCryptoLib.jar",
            "system/system/priv-app/KmxService"
        ]
        for p in paths:
            self.secure_delete(os.path.join(self.target_dir, p))
        if sys.stdout and sys.stdout.isatty(): print(f"\n{Fore.GREEN}[+] Fabric Crypto removed.")

    def start_kick(self):
        if sys.stdout and sys.stdout.isatty(): print(f"{Fore.CYAN}[*] Multi-threaded Debloat starting...")
        app_sub_dirs = ["system/system/app", "system/system/priv-app", "product/app", "product/priv-app"]
        targets = []
        for app in self.debloat_apps:
            for sub_dir in app_sub_dirs:
                targets.append(os.path.join(self.target_dir, sub_dir, app))
        with ThreadPoolExecutor(max_workers=15) as executor:
            executor.map(self.secure_delete, targets)

    def extra_cleanup(self):
        self.animate_loading("Final Optimization")
        extra_paths = [
            "system/system/hidden", "system/system/preload", "system/system/tts",
            "system/system/etc/mediasearch", "product/app/Gmail2/oat",
            "product/app/YouTube/oat", "system/system/etc/init/boot-image.prof"
        ]
        for p in extra_paths:
            self.secure_delete(os.path.join(self.target_dir, p))

    def run(self):
        self.banner()
        
        # حل مشكلة الانهيار: التحقق من وجود Terminal أو Input
        if len(sys.argv) > 1:
            self.target_dir = sys.argv[1]
        else:
            if sys.stdin and sys.stdin.isatty():
                try:
                    self.target_dir = input(f"{Fore.YELLOW}Enter the firmware path: {Style.RESET_ALL}")
                except EOFError:
                    self.target_dir = os.getcwd()
            else:
                # إذا تم التشغيل كـ EXE صامت، نستخدم المجلد الحالي تلقائياً
                self.target_dir = os.getcwd()

        if not os.path.exists(self.target_dir):
            if sys.stdout and sys.stdout.isatty():
                print(f"{Fore.RED}[!] Error: Path '{self.target_dir}' not found.")
            return

        start_time = time.time()
        self.start_kick()
        self.remove_esim_files()
        self.remove_fabric_crypto()
        self.extra_cleanup()
        duration = round(time.time() - start_time, 2)
        
        if sys.stdout and sys.stdout.isatty():
            print(f"\n{Fore.CYAN}{'='*60}")
            print(f"{Fore.GREEN}   Deleted Items : {self.deleted_count} | Time: {duration}s")
            print(f"{Fore.MAGENTA}   Status        : Optimized by Ahmed Younis")
            print(f"{Fore.CYAN}{'='*60}")

if __name__ == "__main__":
    tool = AhmedYounisDebloater()
    tool.run()
