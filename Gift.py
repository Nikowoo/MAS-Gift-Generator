import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser

# Gift data
GIFTS = {
    "Ribbons": [
        "blackribbon",
        "blueribbon",
        "darkpurpleribbon",
        "emeraldribbon",
        "grayribbon",
        "greenribbon",
        "lightpurpleribbon",
        "peachribbon",
        "pinkribbon",
        "platinumribbon",
        "redribbon",
        "rubyribbon",
        "sapphireribbon",
        "silverribbon",
        "tealribbon",
        "yellowribbon"
    ],

    "Sprite Ribbons": [
        "bisexualpridethemedribbon",
        "blackandwhiteribbon",
        "blueandwhitestripedribbon",
        "bronzeribbon",
        "brownribbon",
        "gradientribbon",
        "lowpolygradientribbon",
        "pinkandwhitestripedribbon",
        "rainbowgradientribbon",
        "starryblackskyribbon",
        "starryredskyribbon",
        "transgenderpridethemedribbon",
        "whiteonredpolkadotribbon",
        "coffeeribbon",
        "goldribbon",
        "hotpinkribbon",
        "lilacribbon",
        "limegreenribbon",
        "navyblueribbon",
        "orangeribbon",
        "royalpurpleribbon",
        "skyblueribbon",
        "blackbow",
        "8purpleribbon",
        "8redribbon",
        "amdekamberribbon",
        "gameboygreenribbon",
        "supergameboygreenribbon",
        "8blueribbon",
        "8emeraldribbon",
        "8whiteribbon",
        "bluebunnyscrunchie",
        "stypeblackribbon",
        "stypeblueribbon",
        "stypedarkpurpleribbon",
        "stypedefribbon",
        "stypeemeraldribbon",
        "stypegrayribbon",
        "stypegreenribbon",
        "stypelightpurpleribbon",
        "stypepeachribbon",
        "stypepinkribbon",
        "stypeplatinumribbon",
        "styperedribbon",
        "styperubyribbon",
        "stypesapphireribbon",
        "stypesilverribbon",
        "stypetealribbon",
        "stypewineribbon",
        "stypeyellowribbon"
    ],

    "Sprite Hair Clips": [
        "bathairclip",
        "crescentmoonhairclip",
        "ghosthairclip",
        "pumpkinhairclip",
        "cherryhairclip",
        "hearthairclip",
        "musicnotehairclip"
    ],

    "Sprite Shirts": [
        "putonahappyface",
        "blueshirt",
        "greendress",
        "greenhoodie",
        "brownwinterjacket",
        "resthereshirt",
        "bluesweatervest",
        "tanktop",
        "beigeturtleneck",
        "2bcosplay",
        "pinkkimono",
        "blackandwhitestripedpullover",
        "wineasymmetricalpullover",
        "pinkshirt",
        "whiteandnavybluedress"
    ],

    "Sprite Necklaces": [
        "anchor_necklace",
        "animalcrossing_necklace",
        "cactus_necklace",
        "goldchain_necklace",
        "snailshell_necklace",
        "star_necklace",
        "sunflower_necklace",
        "triforce_necklace",
        "heartchoker",
        "floweredchoker",
        "simplechoker"
    ],

    "All Year": [
        "coffee",
        "hotchocolate",
        "fudge",
        "roses",
        "chocolates"
    ],

    "One Time": [
        "quetzalplushie",
        "justmonikathermos"
    ],

    "Halloween": [
        "candy",
        "candycorn"
    ],

    "Christmas": [
        "christmascookies",
        "candycane"
    ],
}

GIFT_GUIDE_URL = (
    "https://github.com/Monika-After-Story/MonikaModDev/wiki/Gift-Giving-Guide#gifts"
)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller stores temp path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class GiftGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monika After Story Gift Generator")
        self.root.resizable(False, False)

        # Load icon correctly whether running as .py or .exe
        try:
            icon_path = resource_path("MAS.ico")
            self.root.iconbitmap(icon_path)
        except Exception:
            pass

        self.target_dir = tk.StringVar()
        self.folder_vars = {name: tk.BooleanVar(value=True) for name in GIFTS}

        self.sort_into_folders = tk.BooleanVar(value=True)
        self.overwrite_files = tk.BooleanVar(value=True)
        self.open_after = tk.BooleanVar(value=False)
        self.confirm_before = tk.BooleanVar(value=True)

        padding = {"padx": 8, "pady": 6}

        main_frame = tk.Frame(root, padx=15, pady=15)
        main_frame.pack()

        # Directory selection
        tk.Label(main_frame, text="Target directory:").grid(row=0, column=0, sticky="w")
        tk.Entry(main_frame, textvariable=self.target_dir, width=45).grid(row=1, column=0, **padding)
        tk.Button(main_frame, text="Browse", command=self.browse).grid(row=1, column=1, **padding)

        # Options frame
        options_frame = tk.LabelFrame(main_frame, text="Options", padx=10, pady=10)
        options_frame.grid(row=2, column=0, columnspan=2, sticky="we", **padding)

        tk.Checkbutton(options_frame, text="Sort gifts into folders", variable=self.sort_into_folders).pack(anchor="w")
        tk.Checkbutton(options_frame, text="Overwrite existing files", variable=self.overwrite_files).pack(anchor="w")
        tk.Checkbutton(options_frame, text="Confirm before generating files", variable=self.confirm_before).pack(anchor="w")
        tk.Checkbutton(options_frame, text="Open folder after generation", variable=self.open_after).pack(anchor="w")

        # Gift categories frame
        categories_frame = tk.LabelFrame(main_frame, text="Gift categories", padx=10, pady=10)
        categories_frame.grid(row=3, column=0, columnspan=2, sticky="we", **padding)

        for i, name in enumerate(GIFTS):
            cb = tk.Checkbutton(categories_frame, text=name, variable=self.folder_vars[name])
            cb.grid(row=i // 2, column=i % 2, sticky="w", padx=6, pady=3)

        # Generate button
        tk.Button(main_frame, text="Generate Gifts", width=20, command=self.generate).grid(row=4, column=0, columnspan=2, pady=12)

        # Link to guide
        link = tk.Label(main_frame, text="MAS Gift Giving Guide", fg="blue", cursor="hand2")
        link.grid(row=5, column=0, columnspan=2)
        link.bind("<Button-1>", lambda e: webbrowser.open(GIFT_GUIDE_URL))

    def browse(self):
        path = filedialog.askdirectory()
        if path:
            self.target_dir.set(path)

    def generate(self):
        base = self.target_dir.get()
        if not base:
            messagebox.showerror("Error", "Please select a directory.")
            return

        planned = []

        for folder, items in GIFTS.items():
            if not self.folder_vars[folder].get():
                continue

            target = base
            if self.sort_into_folders.get():
                target = os.path.join(base, folder)

            for name in items:
                planned.append(os.path.join(target, f"{name}.gift"))

        if self.confirm_before.get():
            if not messagebox.askyesno(
                "Confirm",
                f"{len(planned)} gift files will be generated.\nContinue?"
            ):
                return

        created = 0

        try:
            for path in planned:
                os.makedirs(os.path.dirname(path), exist_ok=True)

                if os.path.exists(path) and not self.overwrite_files.get():
                    continue

                open(path, "w").close()
                created += 1

            messagebox.showinfo(
                "Done",
                f"{created} files created successfully."
            )

            if self.open_after.get():
                os.startfile(base)

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    GiftGeneratorApp(root)
    root.mainloop()



