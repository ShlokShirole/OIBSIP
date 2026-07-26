import tkinter as tk
from tkinter import ttk
from core.generator import generate_password
from core.evaluator import evaluate_strength
from core.history import PasswordHistory

class MainWindow:
    def __init__(self, root):
        self.root = root
        root.title("Password Generator")
        root.geometry("520x700")
        root.configure(bg="#1a1a24")
        root.resizable(False, False)

        # ── State variables ──
        self.length = tk.IntVar(value=10)
        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=False)
        self.password = tk.StringVar(value="PTx1f5DaFX")

        # ── History object ──
        self.history = PasswordHistory()

        # ── Build UI ──
        self._build_ui()

        # Generate initial password (without adding to history)
        self._generate_password(save_history=False)

    def _build_ui(self):
        main = tk.Frame(self.root, bg="#1a1a24")
        main.pack(fill="both", expand=True, padx=20, pady=(20, 10))

        # ─ Password display ─
        pwd_frame = tk.Frame(main, bg="#111118", highlightbackground="#2a2a38", highlightthickness=1)
        pwd_frame.pack(pady=5, fill="x")

        entry = tk.Entry(pwd_frame, textvariable=self.password, font=("Inter", 24, "bold"),
                         bg="#111118", fg="#f0f0f5", bd=0, relief="flat", state="readonly",
                         readonlybackground="#111118")
        entry.pack(side="left", fill="x", expand=True, padx=(10, 5), pady=8)

        copy_btn = tk.Button(pwd_frame, text="📋", font=("Segoe UI", 14), bg="#111118", fg="#7a7a8e",
                             relief="flat", activebackground="#2a2a3a", activeforeground="#e0e0ed",
                             command=self._on_copy)
        copy_btn.pack(side="right", padx=(0, 10), pady=8)

        # ─ Length slider ─
        length_frame = tk.Frame(main, bg="#1a1a24")
        length_frame.pack(pady=(10, 0), fill="x")

        ttk.Label(length_frame, text="Character Length", foreground="#c0c0d0").pack(side="left")
        self.len_value = ttk.Label(length_frame, text="10", foreground="#f0f0f5", font=("Inter", 14, "bold"))
        self.len_value.pack(side="right")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Dark.Horizontal.TScale", background="#1a1a24", troughcolor="#2a2a3a",
                        slidercolor="#4a7cf7", sliderrelief="flat", borderwidth=0)
        scale = ttk.Scale(main, from_=4, to=32, variable=self.length, orient="horizontal",
                          style="Dark.Horizontal.TScale", command=self._on_length_change)
        scale.pack(pady=(5, 10), fill="x")

        # ─ Checkboxes ─
        opts_frame = tk.Frame(main, bg="#1a1a24")
        opts_frame.pack(pady=5, fill="x")

        def make_check(parent, text, var):
            cb = tk.Checkbutton(parent, text=text, variable=var, bg="#1a1a24", fg="#d0d0e0",
                                selectcolor="#1a1a24", activebackground="#1a1a24",
                                activeforeground="#f0f0f5", font=("Inter", 10),
                                relief="flat", bd=0, highlightthickness=0,
                                command=self._on_option_change)
            cb.pack(anchor="w", pady=2)
            return cb

        left = tk.Frame(opts_frame, bg="#1a1a24")
        left.pack(side="left", fill="both", expand=True)
        right = tk.Frame(opts_frame, bg="#1a1a24")
        right.pack(side="right", fill="both", expand=True)

        make_check(left, "Uppercase Letters", self.use_upper)
        make_check(left, "Lowercase Letters", self.use_lower)
        make_check(right, "Numbers", self.use_digits)
        make_check(right, "Symbols", self.use_symbols)

        # ─ Strength display ─
        strength_frame = tk.Frame(main, bg="#111118", highlightbackground="#252533", highlightthickness=1)
        strength_frame.pack(pady=10, fill="x")

        ttk.Label(strength_frame, text="STRENGTH", foreground="#8a8a9e", font=("Inter", 10, "bold"))\
            .pack(side="left", padx=10, pady=10)

        bar_frame = tk.Frame(strength_frame, bg="#111118")
        bar_frame.pack(side="right", padx=10, pady=10)

        self.bars = []
        for _ in range(4):
            bar = tk.Frame(bar_frame, width=26, height=6, bg="#2a2a3a")
            bar.pack(side="left", padx=2)
            self.bars.append(bar)

        self.strength_text = ttk.Label(strength_frame, text="MEDIUM", foreground="#f7b84a",
                                       font=("Inter", 11, "bold"))
        self.strength_text.pack(side="right", padx=(0, 10))

        # ─ Generate button ─
        gen_btn = tk.Button(main, text="GENERATE", font=("Inter", 14, "bold"),
                            bg="#4a7cf7", fg="white", relief="flat", bd=0,
                            activebackground="#5f8cf8", activeforeground="white",
                            cursor="hand2", command=self._on_generate)
        gen_btn.pack(pady=(15, 0), fill="x", ipady=12)

        # ─ History list ─
        ttk.Label(main, text="History", foreground="#c0c0d0", font=("Inter", 10, "bold"))\
            .pack(anchor="w", pady=(15, 5))

        hist_frame = tk.Frame(main, bg="#111118", highlightbackground="#2a2a38", highlightthickness=1)
        hist_frame.pack(fill="both", expand=True, pady=(0, 10))

        scrollbar = tk.Scrollbar(hist_frame, bg="#1a1a24", troughcolor="#111118",
                                 activebackground="#4a7cf7", relief="flat", bd=0,
                                 highlightthickness=0)
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(hist_frame, bg="#111118", fg="#f0f0f5",
                                  font=("Inter", 10), selectbackground="#4a7cf7",
                                  selectforeground="white", relief="flat", bd=0,
                                  highlightthickness=0, yscrollcommand=scrollbar.set)
        self.listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        scrollbar.config(command=self.listbox.yview)

    # ─── Internal helpers ──────────────────────────────────────────

    def _generate_password(self, save_history=False):
        """Generate a new password, optionally saving it to history."""
        length = self.length.get()
        pwd = generate_password(length,
                                self.use_upper.get(),
                                self.use_lower.get(),
                                self.use_digits.get(),
                                self.use_symbols.get())
        self.password.set(pwd)
        self._update_strength(pwd)

        if save_history:
            self.history.add(pwd)
            self._refresh_history()

    def _update_strength(self, pwd):
        label, color = evaluate_strength(pwd,
                                         self.use_upper.get(),
                                         self.use_lower.get(),
                                         self.use_digits.get(),
                                         self.use_symbols.get())
        self.strength_text.config(text=label, foreground=color)

        active = {"WEAK": 2, "MEDIUM": 3, "STRONG": 4}.get(label, 2)
        for i, bar in enumerate(self.bars):
            bar.config(bg=color if i < active else "#2a2a3a")

    def _refresh_history(self):
        self.listbox.delete(0, tk.END)
        for pwd, ts in self.history.get_all():
            self.listbox.insert(tk.END, f"{ts}  {pwd}")

    # ─── Event handlers ─────────────────────────────────────────────

    def _on_length_change(self, value):
        self.len_value.config(text=str(int(float(value))))
        self._generate_password(save_history=False)   # no history

    def _on_option_change(self):
        self._generate_password(save_history=False)   # no history

    def _on_generate(self):
        # User clicked GENERATE → save to history
        self._generate_password(save_history=True)

    def _on_copy(self):
        pwd = self.password.get()
        if pwd:
            self.root.clipboard_clear()
            self.root.clipboard_append(pwd)
            self.root.update()
            # Save to history on copy
            self.history.add(pwd)
            self._refresh_history()
            self.root.title("✅ Copied!")
            self.root.after(1500, lambda: self.root.title("Password Generator"))
