import os
import sys
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk

# دالة التعامل مع الملفات المدمجة (ADB, Fastboot, etc.) داخل الـ EXE
def get_resource_path(relative_path):
    """ الحصول على المسار الصحيح للملفات المدمجة داخل الـ EXE بعد البناء """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class DebloaterTool(ctk.CTk):
    def __init__(self):
        super().__init__()

        # إعدادات الواجهة (Cyber-Prestige Style)
        self.title("QuantumROM Debloater Tool - Windows Edition")
        self.geometry("750x550")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # القائمة الكاملة للتطبيقات بناءً على سكريبت QuantumROM
        self.DEBLOAT_APPS = [
            "SpeechServicesByGoogle", "HMT", "PaymentFramework", "SamsungCalendar", 
            "LiveTranscribe", "DigitalWellbeing", "Maps", "Duo", "Photos", 
            "FactoryCameraFB", "WlanTest", "AssistantShell", "BardShell",
            "YouTube", "Gmail2", "Chrome", "Drive", "Keep", "CalendarGoogle",
            "Books", "Magazines", "Music2", "Videos", "Street", "Velvet"
        ]

        # العناصر الرسومية (UI Elements)
        self.label = ctk.CTkLabel(self, text="Quantum Debloater PRO", font=("Orbitron", 28, "bold"), text_color="#00D4FF")
        self.label.pack(pady=20)

        self.path_frame = ctk.CTkFrame(self)
        self.path_frame.pack(pady=10, padx=20, fill="x")

        self.path_entry = ctk.CTkEntry(self.path_frame, width=500, placeholder_text="Path to Extracted Firmware (e.g. C:/ROM/extracted)")
        self.path_entry.pack(side="left", padx=10, pady=10)

        self.browse_btn = ctk.CTkButton(self.path_frame, text="Browse", width=100, command=self.browse_folder)
        self.browse_btn.pack(side="left", padx=5)

        # الخيارات الإضافية
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.pack(pady=10, padx=20, fill="x")

        self.esim_var = ctk.BooleanVar(value=False)
        self.esim_check = ctk.CTkCheckBox(self.options_frame, text="Remove eSIM Support (Clean System Logs)", variable=self.esim_var, text_color="#FFCC00")
        self.esim_check.pack(pady=5, padx=20, anchor="w")

        self.extra_var = ctk.BooleanVar(value=True)
        self.extra_check = ctk.CTkCheckBox(self.options_frame, text="Clean Fabric Crypto & Hidden Logs", variable=self.extra_var)
        self.extra_check.pack(pady=5, padx=20, anchor="w")

        # منطقة عرض العمليات (Log)
        self.log_text = ctk.CTkTextbox(self, width=700, height=180, font=("Consolas", 12))
        self.log_text.pack(pady=15, padx=20)

        # زر التشغيل
        self.start_btn = ctk.CTkButton(self, text="START DEBLOATING", height=50, font=("Arial", 18, "bold"), 
                                        fg_color="#008000", hover_color="#006400", command=self.start_debloat)
        self.start_btn.pack(pady=10)

        # تذييل الصفحة (Credits)
        self.footer = ctk.CTkLabel(self, text="Developed by: Ahmed Younis (AKRO)", font=("Arial", 10, "italic"))
        self.footer.pack(side="bottom", pady=5)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder_selected)

    def log(self, message):
        self.log_text.insert(tk.END, f">> {message}\n")
        self.log_text.see(tk.END)
        self.update_idletasks()

    def start_debloat(self):
        base_path = self.path_entry.get().strip()
        if not base_path or not os.path.exists(base_path):
            messagebox.showerror("Error", "Please select a valid firmware directory!")
            return

        self.log_text.delete("1.0", tk.END)
        self.log("Initializing Quantum Debloat Engine...")

        # 1. تنظيف التطبيقات من كل المسارات الممكنة
        partitions = ["system/system/app", "system/system/priv-app", "product/app", "product/priv-app", "system_ext/app", "system_ext/priv-app"]
        
        for app in self.DEBLOAT_APPS:
            for part in partitions:
                target = os.path.join(base_path, part, app)
                if os.path.exists(target):
                    try:
                        shutil.rmtree(target)
                        self.log(f"[KICKED] {app} from {part}")
                    except Exception as e:
                        self.log(f"[FAIL] {app}: {str(e)}")

        # 2. حذف ملفات الـ eSIM (المسارات الدقيقة من السكريبت الأصلي)
        if self.esim_var.get():
            self.log("Executing eSIM Purge...")
            self.remove_esim(base_path)

        # 3. تنظيف ملفات الـ Fabric والملفات الزائدة
        if self.extra_var.get():
            self.remove_extra_stuff(base_path)

        self.log("-----------------------------------------")
        self.log("STAGING COMPLETE: Firmware is now Debloated!")
        messagebox.showinfo("Success", "Process Finished Successfully!")

    def remove_esim(self, base_path):
        esim_files = [
            "system/system/etc/autoinstalls/autoinstalls-com.google.android.euicc",
            "system/system/etc/default-permissions/default-permissions-com.google.android.euicc.xml",
            "system/system/etc/permissions/privapp-permissions-com.samsung.euicc.xml",
            "system/system/etc/permissions/privapp-permissions-com.google.android.app.telephonyui.esim",
            "system/system/etc/permissions/privapp-permissions-com.samsung.android.app.telephonyui.esimclient.xml",
            "system/system/etc/sysconfig/preinstalled-packages-com.samsung.android.app.telephonyui.esimclient.xml",
            "system/system/etc/sysconfig/preinstalled-packages-com.google.android.app.telephonyui.esimkeystring.xml",
            "system/system/priv-app/EsimClient",
            "system/system/priv-app/EsimKeyString"
        ]
        for file_path in esim_files:
            full_path = os.path.join(base_path, file_path)
            if os.path.exists(full_path):
                try:
                    if os.path.isdir(full_path): shutil.rmtree(full_path)
                    else: os.remove(full_path)
                    self.log(f"[REMOVED] eSIM Component: {os.path.basename(file_path)}")
                except: pass

    def remove_extra_stuff(self, base_path):
        extra_paths = [
            "system/system/hidden",
            "system/system/etc/selinux",
            "system/system/recovery-from-boot.p",
            "vendor/operator"
        ]
        for ep in extra_paths:
            target = os.path.join(base_path, ep)
            if os.path.exists(target):
                try:
                    if os.path.isdir(target): shutil.rmtree(target)
                    else: os.remove(target)
                    self.log(f"[CLEAN] Extra Junk: {ep}")
                except: pass

if __name__ == "__main__":
    app = DebloaterTool()
    app.mainloop()
