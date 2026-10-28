import tkinter as tk
from tkinter import messagebox
import random
import webbrowser


# =========================================================
# MEGA ARCADE
# =========================================================

class MegaArcade:
    def __init__(self, root):
        self.root = root
        self.root.title("Muhammad's Mega Arcade")
        self.root.geometry("900x650")
        self.root.configure(bg="#080812")

        self.games = [
            ("🐍", "SNAKE CLASH", self.snake_menu),
            ("🐹", "CAPYBARA CLICKER", self.clicker_game),
            ("🏓", "CAPYBARA PONG", self.pong_game),
            ("🪙", "HEAD OR TAIL", self.coin_game),
            ("🔢", "EVEN OR ODD", self.even_odd_game),
            ("🗺️", "TREASURE HUNT", self.treasure_hunt),
            ("✊", "ROCK PAPER SCISSORS", self.rps_game),
            ("🏎️", "NEON RACER", self.racing_game),
            ("⚡", "CYBER DODGE", self.cyber_dodge_game),
            ("🧠", "MEMORY MATCH", self.memory_match_game),
            ("🚀", "SPACE BLASTER", self.space_blaster_game),
            ("🧱", "BRICK BREAKER", self.brick_breaker_game),
            ("🦘", "JUMP DASH", self.jump_dash_game),
            ("💎", "GEM CATCHER", self.gem_catcher_game),
            ("🔗", "WEBSITE LINKER", self.linker_game)
        ]

        self.show_home()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def title(self, text):
        tk.Label(
            self.root,
            text=text,
            font=("Arial", 30, "bold"),
            fg="#00ffff",
            bg="#080812"
        ).pack(pady=20)

    def button(self, text, command, width=28):
        tk.Button(
            self.root,
            text=text,
            command=command,
            width=width,
            font=("Arial", 13, "bold"),
            bg="#15152b",
            fg="white",
            activebackground="#00ffff",
            activeforeground="black",
            relief="flat",
            padx=10,
            pady=8
        ).pack(pady=5)

    def back_button(self):
        self.button("← BACK TO ARCADE", self.show_home, 22)

    def show_home(self):
        self.root.unbind("<KeyPress-w>")
        self.root.unbind("<KeyPress-s>")
        self.root.unbind("<KeyPress-Up>")
        self.root.unbind("<KeyPress-Down>")
        self.clear()

        # Scrollable arcade menu
        canvas = tk.Canvas(self.root, bg="#080812", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        frame = tk.Frame(canvas, bg="#080812")
        window = canvas.create_window((0, 0), window=frame, anchor="nw")

        def update_scroll(event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(window, width=canvas.winfo_width())

        frame.bind("<Configure>", update_scroll)
        canvas.bind("<Configure>", update_scroll)

        def mouse_wheel(event):
            canvas.yview_scroll(int(-event.delta / 120), "units")

        canvas.bind_all("<MouseWheel>", mouse_wheel)
        canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-3, "units"))
        canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(3, "units"))

        tk.Label(
            frame,
            text="⚡ MUHAMMAD'S",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#080812"
        ).pack(pady=(20, 0))

        tk.Label(
            frame,
            text="MEGA ARCADE",
            font=("Arial", 38, "bold"),
            fg="#00ffff",
            bg="#080812"
        ).pack()

        tk.Label(
            frame,
            text="15 PROJECTS • 1 ARCADE • INFINITE FUN",
            font=("Arial", 11),
            fg="#8888aa",
            bg="#080812"
        ).pack(pady=(0, 15))

        cards = tk.Frame(frame, bg="#080812")
        cards.pack()

        for i, (emoji, name, command) in enumerate(self.games):
            card = tk.Frame(
                cards,
                bg="#111122",
                width=240,
                height=110,
                highlightbackground="#202050",
                highlightthickness=2
            )
            card.grid(row=i // 3, column=i % 3, padx=8, pady=8)
            card.pack_propagate(False)

            tk.Label(card, text=emoji, font=("Arial", 30), bg="#111122").pack(pady=(8, 0))
            tk.Button(
                card,
                text=name,
                command=command,
                font=("Arial", 10, "bold"),
                bg="#111122",
                fg="white",
                activebackground="#00ffff",
                activeforeground="black",
                relief="flat"
            ).pack()

        tk.Label(
            frame,
            text="Scroll to see all games • Built in Python 🐍",
            font=("Arial", 10),
            fg="#555577",
            bg="#080812"
        ).pack(pady=20)

    def snake_menu(self):
        self.clear()
        self.title("🐍 SNAKE CLASH")

        tk.Label(
            self.root,
            text="Eat the food • Grow • Survive",
            font=("Arial", 14),
            fg="white",
            bg="#080812"
        ).pack(pady=5)

        self.button("▶ START SNAKE", self.start_snake)
        self.button("← BACK", self.show_home)

    def start_snake(self):
        self.clear()

        self.snake_canvas = tk.Canvas(
            self.root,
            width=800,
            height=560,
            bg="black",
            highlightthickness=0
        )
        self.snake_canvas.pack()

        self.snake_score = 0
        self.snake_direction = "Right"
        self.snake_running = True

        self.snake_body = [
            [400, 280],
            [380, 280],
            [360, 280]
        ]

        self.snake_food = [
            random.randrange(20, 780, 20),
            random.randrange(20, 540, 20)
        ]

        self.snake_canvas.focus_set()

        self.snake_canvas.bind("<Up>", lambda e: self.change_snake_direction("Up"))
        self.snake_canvas.bind("<Down>", lambda e: self.change_snake_direction("Down"))
        self.snake_canvas.bind("<Left>", lambda e: self.change_snake_direction("Left"))
        self.snake_canvas.bind("<Right>", lambda e: self.change_snake_direction("Right"))

        self.snake_draw()
        self.snake_move()

    def change_snake_direction(self, direction):
        opposite = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left"
        }

        if direction != opposite[self.snake_direction]:
            self.snake_direction = direction

    def snake_draw(self):
        self.snake_canvas.delete("all")

        self.snake_canvas.create_text(
            400,
            15,
            text=f"SCORE: {self.snake_score}",
            fill="cyan",
            font=("Arial", 18, "bold")
        )

        x, y = self.snake_food

        self.snake_canvas.create_oval(
            x - 8,
            y - 8,
            x + 8,
            y + 8,
            fill="red",
            outline=""
        )

        for i, (x, y) in enumerate(self.snake_body):
            if i == 0:
                self.snake_canvas.create_rectangle(
                    x - 9,
                    y - 9,
                    x + 9,
                    y + 9,
                    fill="lime",
                    outline=""
                )
            else:
                self.snake_canvas.create_rectangle(
                    x - 8,
                    y - 8,
                    x + 8,
                    y + 8,
                    fill="green",
                    outline=""
                )

    def snake_move(self):
        if not self.snake_running:
            return

        head_x, head_y = self.snake_body[0]

        if self.snake_direction == "Up":
            head_y -= 20
        elif self.snake_direction == "Down":
            head_y += 20
        elif self.snake_direction == "Left":
            head_x -= 20
        elif self.snake_direction == "Right":
            head_x += 20

        new_head = [head_x, head_y]

        if (
            head_x < 0
            or head_x >= 800
            or head_y < 20
            or head_y >= 560
            or new_head in self.snake_body
        ):
            self.snake_game_over()
            return

        self.snake_body.insert(0, new_head)

        # =================================================
        # FOOD FIX
        # =================================================
        if new_head == self.snake_food:
            self.snake_score += 1

            self.snake_food = [
                random.randrange(20, 780, 20),
                random.randrange(40, 540, 20)
            ]

            while self.snake_food in self.snake_body:
                self.snake_food = [
                    random.randrange(20, 780, 20),
                    random.randrange(40, 540, 20)
                ]
        else:
            self.snake_body.pop()

        self.snake_draw()

        self.root.after(90, self.snake_move)

    def snake_game_over(self):
        self.snake_running = False

        self.snake_canvas.create_text(
            400,
            250,
            text="GAME OVER",
            fill="red",
            font=("Arial", 38, "bold")
        )

        self.snake_canvas.create_text(
            400,
            300,
            text=f"Score: {self.snake_score}",
            fill="white",
            font=("Arial", 20, "bold")
        )

        tk.Button(
            self.root,
            text="PLAY AGAIN",
            command=self.start_snake,
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="BACK",
            command=self.show_home,
            font=("Arial", 12, "bold")
        ).pack()

    # =====================================================
    # CAPYBARA CLICKER
    # =====================================================

    def clicker_game(self):
        self.clear()
        self.title("🐹 CAPYBARA CLICKER")

        self.clicks = 0
        self.click_power = 1
        self.click_level = 1
        self.upgrade_cost = 25

        self.click_score = tk.Label(
            self.root,
            text="Clicks: 0",
            font=("Arial", 24, "bold"),
            fg="cyan",
            bg="#080812"
        )
        self.click_score.pack(pady=10)

        self.capy_button = tk.Button(
            self.root,
            text="🐹\nCAPYBARA",
            font=("Arial", 30, "bold"),
            width=10,
            height=4,
            bg="#8B5A2B",
            fg="white",
            command=self.click_capybara
        )
        self.capy_button.pack(pady=15)

        self.level_label = tk.Label(
            self.root,
            text="Level: 1   Power: +1",
            font=("Arial", 15),
            fg="white",
            bg="#080812"
        )
        self.level_label.pack()

        self.upgrade_button = tk.Button(
            self.root,
            text="UPGRADE (+1) — Cost: 25",
            command=self.upgrade_clicker,
            font=("Arial", 13, "bold")
        )
        self.upgrade_button.pack(pady=15)

        self.back_button()

    def click_capybara(self):
        self.clicks += self.click_power
        self.update_clicker()

    def upgrade_clicker(self):
        if self.clicks >= self.upgrade_cost:
            self.clicks -= self.upgrade_cost
            self.click_power += 1
            self.click_level += 1
            self.upgrade_cost = int(self.upgrade_cost * 1.7)
            self.update_clicker()
        else:
            messagebox.showinfo(
                "Not enough clicks",
                f"You need {self.upgrade_cost} clicks!"
            )

    def update_clicker(self):
        self.click_score.config(
            text=f"Clicks: {self.clicks}"
        )

        self.level_label.config(
            text=f"Level: {self.click_level}   Power: +{self.click_power}"
        )

        self.upgrade_button.config(
            text=f"UPGRADE (+1) — Cost: {self.upgrade_cost}"
        )

    # =====================================================
    # CAPYBARA PONG
    # =====================================================

    def pong_game(self):
        self.clear()

        self.pong_canvas = tk.Canvas(
            self.root,
            width=850,
            height=550,
            bg="#123512",
            highlightthickness=0
        )
        self.pong_canvas.pack()

        self.pong_left_y = 250
        self.pong_right_y = 250
        self.pong_ball_x = 425
        self.pong_ball_y = 275
        self.pong_dx = 5
        self.pong_dy = 4
        self.pong_left_score = 0
        self.pong_right_score = 0
        self.pong_running = True

        self.root.bind("<KeyPress-w>", lambda e: self.move_paddle("left", -30))
        self.root.bind("<KeyPress-s>", lambda e: self.move_paddle("left", 30))
        self.root.bind("<KeyPress-Up>", lambda e: self.move_paddle("right", -30))
        self.root.bind("<KeyPress-Down>", lambda e: self.move_paddle("right", 30))

        self.root.focus_force()
        self.pong_loop()

    def move_paddle(self, side, amount):
        if side == "left":
            self.pong_left_y += amount
            self.pong_left_y = max(70, min(480, self.pong_left_y))
        else:
            self.pong_right_y += amount
            self.pong_right_y = max(70, min(480, self.pong_right_y))

    def pong_loop(self):
        if not self.pong_running:
            return

        self.pong_ball_x += self.pong_dx
        self.pong_ball_y += self.pong_dy

        if self.pong_ball_y <= 15 or self.pong_ball_y >= 535:
            self.pong_dy *= -1

        if (
            self.pong_ball_x <= 55
            and abs(self.pong_ball_y - self.pong_left_y) < 75
            and self.pong_dx < 0
        ):
            self.pong_dx *= -1

        if (
            self.pong_ball_x >= 795
            and abs(self.pong_ball_y - self.pong_right_y) < 75
            and self.pong_dx > 0
        ):
            self.pong_dx *= -1

        if self.pong_ball_x < 0:
            self.pong_right_score += 1
            self.pong_reset_ball()

        if self.pong_ball_x > 850:
            self.pong_left_score += 1
            self.pong_reset_ball()

        self.draw_pong()

        if (
            self.pong_left_score >= 5
            or self.pong_right_score >= 5
        ):
            self.pong_running = False
            self.pong_canvas.create_text(
                425,
                275,
                text="GAME OVER",
                fill="white",
                font=("Arial", 35, "bold")
            )

            self.root.after(1200, self.show_home)
            return

        self.root.after(16, self.pong_loop)

    def pong_reset_ball(self):
        self.pong_ball_x = 425
        self.pong_ball_y = 275

        self.pong_dx = random.choice([-5, 5])
        self.pong_dy = random.choice([-4, 4])

    def draw_pong(self):
        self.pong_canvas.delete("all")

        self.pong_canvas.create_line(
            425,
            0,
            425,
            550,
            fill="white",
            dash=(5, 10)
        )

        self.pong_canvas.create_text(
            425,
            30,
            text=f"{self.pong_left_score}        {self.pong_right_score}",
            fill="white",
            font=("Arial", 25, "bold")
        )

        self.pong_canvas.create_text(
            425,
            525,
            text="🐹 CAPYBARA PONG 🐹",
            fill="white",
            font=("Arial", 14, "bold")
        )

        self.pong_canvas.create_rectangle(
            25,
            self.pong_left_y - 65,
            45,
            self.pong_left_y + 65,
            fill="brown"
        )

        self.pong_canvas.create_text(
            35,
            self.pong_left_y,
            text="🐹",
            font=("Arial", 18)
        )

        self.pong_canvas.create_rectangle(
            805,
            self.pong_right_y - 65,
            825,
            self.pong_right_y + 65,
            fill="brown"
        )

        self.pong_canvas.create_text(
            815,
            self.pong_right_y,
            text="🐹",
            font=("Arial", 18)
        )

        self.pong_canvas.create_oval(
            self.pong_ball_x - 10,
            self.pong_ball_y - 10,
            self.pong_ball_x + 10,
            self.pong_ball_y + 10,
            fill="white"
        )

    # =====================================================
    # HEAD OR TAIL
    # =====================================================

    def coin_game(self):
        self.clear()
        self.title("🪙 HEAD OR TAIL")

        self.coin_score = 0

        self.coin_label = tk.Label(
            self.root,
            text="Score: 0",
            font=("Arial", 20, "bold"),
            fg="cyan",
            bg="#080812"
        )
        self.coin_label.pack(pady=15)

        tk.Button(
            self.root,
            text="🪙 HEAD",
            command=lambda: self.flip_coin("Heads"),
            font=("Arial", 18, "bold"),
            width=15,
            pady=10
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="🪙 TAIL",
            command=lambda: self.flip_coin("Tails"),
            font=("Arial", 18, "bold"),
            width=15,
            pady=10
        ).pack(pady=10)

        self.back_button()

    def flip_coin(self, choice):
        result = random.choice(["Heads", "Tails"])

        if choice == result:
            self.coin_score += 1
            messagebox.showinfo(
                "YOU WIN!",
                f"The coin was {result}!\n+1 point 🎉"
            )
        else:
            self.coin_score = 0
            messagebox.showinfo(
                "Try Again",
                f"The coin was {result}!"
            )

        self.coin_label.config(
            text=f"Score: {self.coin_score}"
        )

    # =====================================================
    # EVEN OR ODD
    # =====================================================

    def even_odd_game(self):
        self.clear()
        self.title("🔢 EVEN OR ODD")

        self.eo_streak = 0

        self.eo_number = random.randint(1, 100)

        self.eo_number_label = tk.Label(
            self.root,
            text=str(self.eo_number),
            font=("Arial", 60, "bold"),
            fg="cyan",
            bg="#080812"
        )
        self.eo_number_label.pack(pady=20)

        self.eo_streak_label = tk.Label(
            self.root,
            text="Streak: 0",
            font=("Arial", 18),
            fg="white",
            bg="#080812"
        )
        self.eo_streak_label.pack()

        tk.Button(
            self.root,
            text="EVEN",
            command=lambda: self.check_even_odd("Even"),
            font=("Arial", 18, "bold"),
            width=15,
            pady=10
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="ODD",
            command=lambda: self.check_even_odd("Odd"),
            font=("Arial", 18, "bold"),
            width=15,
            pady=10
        ).pack(pady=10)

        self.back_button()

    def check_even_odd(self, choice):
        correct = (
            "Even"
            if self.eo_number % 2 == 0
            else "Odd"
        )

        if choice == correct:
            self.eo_streak += 1
            messagebox.showinfo("Correct!", "🔥 Nice!")
        else:
            self.eo_streak = 0
            messagebox.showinfo(
                "Wrong!",
                f"{self.eo_number} is {correct}."
            )

        self.eo_number = random.randint(1, 100)

        self.eo_number_label.config(
            text=str(self.eo_number)
        )

        self.eo_streak_label.config(
            text=f"Streak: {self.eo_streak}"
        )

    # =====================================================
    # TREASURE HUNT
    # =====================================================

    def treasure_hunt(self):
        self.clear()
        self.title("🗺️ TREASURE HUNT")

        self.treasure_score = 0

        tk.Label(
            self.root,
            text="🌴 THE LOST TEMPLE 🌴",
            font=("Arial", 22, "bold"),
            fg="lime",
            bg="#080812"
        ).pack(pady=10)

        self.treasure_text = tk.Label(
            self.root,
            text="You found an ancient temple!\nChoose a path to find the hidden treasure.",
            font=("Arial", 15),
            fg="white",
            bg="#080812"
        )
        self.treasure_text.pack(pady=20)

        self.treasure_score_label = tk.Label(
            self.root,
            text="Treasure Score: 0",
            font=("Arial", 18, "bold"),
            fg="cyan",
            bg="#080812"
        )
        self.treasure_score_label.pack(pady=10)

        self.button("🕯️ DARK TUNNEL", lambda: self.choose_treasure(0))
        self.button("🌉 BROKEN BRIDGE", lambda: self.choose_treasure(1))
        self.button("🚪 GOLDEN DOOR", lambda: self.choose_treasure(2))

        self.back_button()

    def choose_treasure(self, choice):
        result = random.randint(0, 2)

        if choice == result:
            self.treasure_score += 2
            messagebox.showinfo(
                "💰 TREASURE FOUND!",
                "You discovered the ancient treasure!\n+2 points! 🎉"
            )
        elif random.randint(1, 2) == 1:
            self.treasure_score = max(0, self.treasure_score - 1)
            messagebox.showwarning(
                "💥 TRAP!",
                "Oh no! You triggered a temple trap!\n-1 point."
            )
        else:
            messagebox.showinfo(
                "🌴 LOST PATH",
                "The path led back to the entrance.\nTry another path!"
            )

        self.treasure_score_label.config(
            text=f"Treasure Score: {self.treasure_score}"
        )

    # =====================================================
    # ROCK PAPER SCISSORS
    # =====================================================

    def rps_game(self):
        self.clear()
        self.title("✊ ROCK PAPER SCISSORS")

        self.rps_player = 0
        self.rps_computer = 0

        self.rps_score = tk.Label(
            self.root,
            text="You: 0    Computer: 0",
            font=("Arial", 20, "bold"),
            fg="cyan",
            bg="#080812"
        )
        self.rps_score.pack(pady=20)

        self.rps_result = tk.Label(
            self.root,
            text="Choose your move!",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#080812"
        )
        self.rps_result.pack(pady=20)

        self.button("✊ ROCK", lambda: self.play_rps("Rock"))
        self.button("📄 PAPER", lambda: self.play_rps("Paper"))
        self.button("✌️ SCISSORS", lambda: self.play_rps("Scissors"))

        self.back_button()

    def play_rps(self, player):
        computer = random.choice(["Rock", "Paper", "Scissors"])

        if player == computer:
            result = "DRAW! 🤝"
        elif (
            (player == "Rock" and computer == "Scissors")
            or (player == "Paper" and computer == "Rock")
            or (player == "Scissors" and computer == "Paper")
        ):
            self.rps_player += 1
            result = "YOU WIN! 🔥"
        else:
            self.rps_computer += 1
            result = "COMPUTER WINS! 🤖"

        self.rps_result.config(
            text=f"You: {player}\nComputer: {computer}\n\n{result}"
        )

        self.rps_score.config(
            text=f"You: {self.rps_player}    Computer: {self.rps_computer}"
        )

    # =====================================================
    # NEON RACER
    # =====================================================

    def racing_game(self):
        self.clear()

        self.race_canvas = tk.Canvas(
            self.root, width=800, height=560,
            bg="#151515", highlightthickness=0
        )
        self.race_canvas.pack()
        self.race_canvas.focus_set()

        self.race_running = True
        self.race_score = 0
        self.race_speed = 7
        self.race_player_x = 400
        self.race_player_y = 480

        self.race_enemies = [
            [250, -80],
            [550, -300],
            [400, -520]
        ]

        self.race_canvas.bind("<Left>", lambda e: self.move_racer(-25))
        self.race_canvas.bind("<Right>", lambda e: self.move_racer(25))

        self.draw_race()
        self.race_loop()

    def move_racer(self, amount):
        if self.race_running:
            self.race_player_x += amount
            self.race_player_x = max(130, min(670, self.race_player_x))

    def draw_race(self):
        self.race_canvas.delete("all")

        self.race_canvas.create_rectangle(
            100, 0, 700, 560, fill="#303030", outline=""
        )
        self.race_canvas.create_rectangle(
            95, 0, 105, 560, fill="yellow", outline=""
        )
        self.race_canvas.create_rectangle(
            695, 0, 705, 560, fill="yellow", outline=""
        )

        for y in range(-40, 600, 80):
            road_y = (y + self.race_score * self.race_speed) % 640 - 40
            self.race_canvas.create_rectangle(
                295, road_y, 305, road_y + 40, fill="white", outline=""
            )
            self.race_canvas.create_rectangle(
                495, road_y, 505, road_y + 40, fill="white", outline=""
            )

        self.draw_car(
            self.race_player_x, self.race_player_y, "cyan"
        )

        for x, y in self.race_enemies:
            self.draw_car(x, y, "red")

        self.race_canvas.create_text(
            400, 25,
            text=f"🏎️ NEON RACER   SCORE: {self.race_score}",
            fill="cyan", font=("Arial", 18, "bold")
        )
        self.race_canvas.create_text(
            400, 540, text="← → MOVE",
            fill="white", font=("Arial", 13, "bold")
        )

    def draw_car(self, x, y, body_color):
        self.race_canvas.create_rectangle(
            x - 25, y - 35, x + 25, y + 35,
            fill=body_color, outline="white", width=2
        )
        self.race_canvas.create_rectangle(
            x - 17, y - 20, x + 17, y,
            fill="#111122", outline=""
        )
        self.race_canvas.create_oval(
            x - 20, y + 18, x - 8, y + 30, fill="black"
        )
        self.race_canvas.create_oval(
            x + 8, y + 18, x + 20, y + 30, fill="black"
        )

    def race_collision(self, x, y):
        return (
            abs(x - self.race_player_x) < 45
            and abs(y - self.race_player_y) < 60
        )

    def race_loop(self):
        if not self.race_running:
            return

        for enemy in self.race_enemies:
            enemy[1] += self.race_speed

            if enemy[1] > 620:
                enemy[1] = random.randint(-500, -100)
                enemy[0] = random.choice([200, 300, 400, 500, 600])
                self.race_score += 1

            if self.race_collision(enemy[0], enemy[1]):
                self.race_running = False
                self.draw_race()

                self.race_canvas.create_text(
                    400, 250, text="CRASH! 💥",
                    fill="red", font=("Arial", 40, "bold")
                )
                self.race_canvas.create_text(
                    400, 300, text=f"Score: {self.race_score}",
                    fill="white", font=("Arial", 20, "bold")
                )

                tk.Button(
                    self.root, text="RACE AGAIN",
                    command=self.racing_game,
                    font=("Arial", 12, "bold")
                ).pack(pady=5)

                tk.Button(
                    self.root, text="BACK",
                    command=self.show_home,
                    font=("Arial", 12, "bold")
                ).pack()
                return

        self.draw_race()
        self.root.after(30, self.race_loop)


    # =====================================================
    # OOZY LAB
    # =====================================================

    def oozy_lab_game(self):
        self.clear()

        self.oozy_canvas = tk.Canvas(
            self.root, width=800, height=560,
            bg="#10101c", highlightthickness=0
        )
        self.oozy_canvas.pack()
        self.oozy_canvas.focus_set()

        self.oozy_level = 1
        self.oozy_score = 0
        self.oozy_keys = set()
        self.oozy_running = True

        self.oozy_levels = [
            {
                "start": (80, 450),
                "exit": (720, 90),
                "moon": (590, 115),
                "platforms": [
                    (0, 510, 800, 50),
                    (60, 420, 210, 20),
                    (330, 350, 180, 20),
                    (570, 270, 170, 20),
                    (390, 190, 140, 20),
                    (650, 120, 100, 20)
                ],
                "hazards": [
                    (275, 495, 325, 510),
                    (510, 335, 570, 350)
                ]
            },
            {
                "start": (70, 450),
                "exit": (700, 90),
                "moon": (455, 175),
                "platforms": [
                    (0, 510, 800, 50),
                    (40, 430, 160, 20),
                    (250, 360, 150, 20),
                    (500, 290, 150, 20),
                    (280, 210, 130, 20),
                    (600, 130, 150, 20)
                ],
                "hazards": [
                    (200, 495, 290, 510),
                    (400, 345, 500, 360),
                    (650, 495, 740, 510)
                ]
            },
            {
                "start": (70, 450),
                "exit": (700, 80),
                "moon": (315, 125),
                "platforms": [
                    (0, 510, 800, 50),
                    (50, 430, 120, 20),
                    (220, 360, 120, 20),
                    (430, 300, 120, 20),
                    (180, 220, 150, 20),
                    (400, 150, 130, 20),
                    (630, 100, 120, 20)
                ],
                "hazards": [
                    (170, 495, 220, 510),
                    (340, 345, 430, 360),
                    (550, 495, 650, 510)
                ]
            }
        ]

        self.oozy_reset()

        self.oozy_canvas.bind("<KeyPress>", self.oozy_key_down)
        self.oozy_canvas.bind("<KeyRelease>", self.oozy_key_up)
        self.oozy_canvas.bind("<r>", lambda e: self.oozy_reset())
        self.oozy_canvas.bind("<Escape>", lambda e: self.show_home())

        self.oozy_loop()

    def oozy_reset(self):
        level = self.oozy_levels[self.oozy_level - 1]
        self.oozy_x, self.oozy_y = level["start"]
        self.oozy_vx = 0
        self.oozy_vy = 0
        self.oozy_on_ground = False
        self.oozy_collected = False
        self.oozy_running = True
        self.oozy_draw()

    def oozy_key_down(self, event):
        self.oozy_keys.add(event.keysym.lower())

    def oozy_key_up(self, event):
        self.oozy_keys.discard(event.keysym.lower())

    def oozy_rects_overlap(self, a, b):
        return (
            a[0] < b[2] and
            a[2] > b[0] and
            a[1] < b[3] and
            a[3] > b[1]
        )

    def oozy_loop(self):
        if not self.oozy_running:
            self.oozy_draw()
            return

        level = self.oozy_levels[self.oozy_level - 1]

        left = "left" in self.oozy_keys or "a" in self.oozy_keys
        right = "right" in self.oozy_keys or "d" in self.oozy_keys
        jump = "up" in self.oozy_keys or "w" in self.oozy_keys

        self.oozy_vx = 0
        if left:
            self.oozy_vx = -5
        if right:
            self.oozy_vx = 5

        if jump and self.oozy_on_ground:
            self.oozy_vy = -12
            self.oozy_on_ground = False

        old_y = self.oozy_y
        self.oozy_vy += 0.55

        self.oozy_x += self.oozy_vx
        self.oozy_x = max(15, min(785, self.oozy_x))

        self.oozy_y += self.oozy_vy
        self.oozy_on_ground = False

        player = (
            self.oozy_x - 16, self.oozy_y - 16,
            self.oozy_x + 16, self.oozy_y + 16
        )

        for px1, py1, px2, py2 in level["platforms"]:
            platform = (px1, py1, px2, py2)

            if self.oozy_rects_overlap(player, platform):
                if old_y + 16 <= py1 and self.oozy_vy >= 0:
                    self.oozy_y = py1 - 16
                    self.oozy_vy = 0
                    self.oozy_on_ground = True
                elif old_y - 16 >= py2 and self.oozy_vy < 0:
                    self.oozy_y = py2 + 16
                    self.oozy_vy = 0

        player = (
            self.oozy_x - 16, self.oozy_y - 16,
            self.oozy_x + 16, self.oozy_y + 16
        )

        for hx1, hy1, hx2, hy2 in level["hazards"]:
            if self.oozy_rects_overlap(player, (hx1, hy1, hx2, hy2)):
                self.oozy_reset()
                return

        if self.oozy_y > 590:
            self.oozy_reset()
            return

        mx, my = level["moon"]
        if not self.oozy_collected:
            if ((self.oozy_x - mx) ** 2 + (self.oozy_y - my) ** 2) ** 0.5 < 35:
                self.oozy_collected = True
                self.oozy_score += 100

        ex, ey = level["exit"]
        if (
            self.oozy_collected and
            ((self.oozy_x - ex) ** 2 + (self.oozy_y - ey) ** 2) ** 0.5 < 40
        ):
            self.oozy_score += 250

            if self.oozy_level < len(self.oozy_levels):
                self.oozy_level += 1
                self.oozy_reset()
                return
            else:
                self.oozy_running = False

        self.oozy_draw()
        self.root.after(25, self.oozy_loop)

    def oozy_draw(self):
        self.oozy_canvas.delete("all")

        level = self.oozy_levels[self.oozy_level - 1]

        self.oozy_canvas.create_text(
            400, 18,
            text=f"🧪 OOZY LAB    LEVEL {self.oozy_level}    SCORE: {self.oozy_score}",
            fill="#00ffff",
            font=("Arial", 18, "bold")
        )

        for x1, y1, x2, y2 in level["platforms"]:
            self.oozy_canvas.create_rectangle(
                x1, y1, x2, y2,
                fill="#26364d",
                outline="#00ffff",
                width=2
            )

        for x1, y1, x2, y2 in level["hazards"]:
            self.oozy_canvas.create_rectangle(
                x1, y1, x2, y2,
                fill="#ff3355",
                outline="#ff6688",
                width=2
            )

        mx, my = level["moon"]
        if not self.oozy_collected:
            self.oozy_canvas.create_oval(
                mx - 15, my - 15, mx + 15, my + 15,
                fill="#ffff66",
                outline="white",
                width=2
            )
            self.oozy_canvas.create_text(
                mx, my,
                text="★",
                fill="#663300",
                font=("Arial", 15, "bold")
            )

        ex, ey = level["exit"]
        self.oozy_canvas.create_rectangle(
            ex - 25, ey - 30, ex + 25, ey + 30,
            outline="#66ff99",
            width=4
        )
        self.oozy_canvas.create_text(
            ex, ey,
            text="EXIT",
            fill="#66ff99",
            font=("Arial", 9, "bold")
        )

        # Original slime character, inspired by the genre rather than copied.
        self.oozy_canvas.create_oval(
            self.oozy_x - 17, self.oozy_y - 15,
            self.oozy_x + 17, self.oozy_y + 17,
            fill="#66ff99",
            outline="white",
            width=2
        )
        self.oozy_canvas.create_oval(
            self.oozy_x - 9, self.oozy_y - 7,
            self.oozy_x - 4, self.oozy_y - 1,
            fill="black"
        )
        self.oozy_canvas.create_oval(
            self.oozy_x + 4, self.oozy_y - 7,
            self.oozy_x + 9, self.oozy_y - 1,
            fill="black"
        )

        self.oozy_canvas.create_text(
            400, 545,
            text="A/D or ← → MOVE    W/↑ JUMP    R RESPAWN    ESC HOME",
            fill="white",
            font=("Arial", 12, "bold")
        )

        if not self.oozy_running:
            self.oozy_canvas.create_text(
                400, 250,
                text="LAB ESCAPED!",
                fill="#66ff99",
                font=("Arial", 40, "bold")
            )
            self.oozy_canvas.create_text(
                400, 300,
                text=f"FINAL SCORE: {self.oozy_score}",
                fill="white",
                font=("Arial", 20, "bold")
            )

            tk.Button(
                self.root,
                text="PLAY AGAIN",
                command=self.oozy_lab_game,
                font=("Arial", 12, "bold")
            ).pack(pady=4)

            tk.Button(
                self.root,
                text="BACK",
                command=self.show_home,
                font=("Arial", 12, "bold")
            ).pack()

    def merge_fruit_game(self):
        self.clear()

        self.merge_canvas = tk.Canvas(
            self.root, width=800, height=560,
            bg="#10101c", highlightthickness=0
        )
        self.merge_canvas.pack()
        self.merge_canvas.focus_set()

        self.merge_running = True
        self.merge_score = 0
        self.merge_fruits = []

        self.merge_names = ["1", "2", "3", "4", "5", "6"]
        self.merge_colors = [
            "#ff3355", "#ff6699", "#ff9900",
            "#ff3333", "#99cc33", "#33cc66"
        ]
        self.merge_sizes = [18, 24, 31, 39, 48, 58]

        self.merge_active_x = 400
        self.merge_active_y = 105
        self.merge_active_level = random.randint(0, 2)
        self.merge_next_level = random.randint(0, 2)
        self.merge_active_dropping = False

        self.merge_canvas.bind("<Left>", lambda e: self.merge_move(-25))
        self.merge_canvas.bind("<Right>", lambda e: self.merge_move(25))
        self.merge_canvas.bind("<space>", lambda e: self.merge_drop())
        self.merge_canvas.bind("<Escape>", lambda e: self.show_home())

        self.merge_draw()
        self.merge_loop()

    def merge_move(self, amount):
        if not self.merge_running or self.merge_active_dropping:
            return

        size = self.merge_sizes[self.merge_active_level]
        self.merge_active_x = max(
            115 + size,
            min(685 - size, self.merge_active_x + amount)
        )
        self.merge_draw()

    def merge_drop(self):
        if not self.merge_running or self.merge_active_dropping:
            return
        self.merge_active_dropping = True

    def merge_loop(self):
        if not self.merge_running:
            return

        if self.merge_active_dropping:
            size = self.merge_sizes[self.merge_active_level]
            target_y = 500 - size

            for ox, oy, ol in self.merge_fruits:
                osize = self.merge_sizes[ol]
                if abs(self.merge_active_x - ox) < (size + osize) * 0.82:
                    target_y = min(target_y, oy - size - osize + 3)

            self.merge_active_y += 9

            if self.merge_active_y >= target_y:
                self.merge_active_y = target_y
                self.merge_fruits.append([
                    self.merge_active_x,
                    self.merge_active_y,
                    self.merge_active_level
                ])

                self.merge_active_level = self.merge_next_level
                self.merge_next_level = random.randint(0, 2)
                self.merge_active_x = 400
                self.merge_active_y = 105
                self.merge_active_dropping = False
                self.merge_combine()

        self.merge_draw()

        for x, y, level in self.merge_fruits:
            if y - self.merge_sizes[level] <= 145:
                self.merge_running = False
                break

        self.root.after(35, self.merge_loop)

    def merge_combine(self):
        changed = True

        while changed:
            changed = False

            for i in range(len(self.merge_fruits)):
                for j in range(i + 1, len(self.merge_fruits)):
                    x1, y1, l1 = self.merge_fruits[i]
                    x2, y2, l2 = self.merge_fruits[j]

                    if l1 != l2 or l1 >= 5:
                        continue

                    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

                    if distance <= self.merge_sizes[l1] * 1.7:
                        nx = (x1 + x2) / 2
                        ny = min(y1, y2)

                        self.merge_fruits.pop(j)
                        self.merge_fruits.pop(i)
                        self.merge_fruits.append([nx, ny, l1 + 1])
                        self.merge_score += (l1 + 1) * 10

                        changed = True
                        break

                if changed:
                    break

        self.merge_fruits.sort(key=lambda f: f[1])

    def merge_draw(self):
        self.merge_canvas.delete("all")

        self.merge_canvas.create_rectangle(
            90, 30, 710, 530,
            outline="#00ffff", width=3
        )

        self.merge_canvas.create_line(
            100, 145, 700, 145,
            fill="#ff3355", dash=(8, 8)
        )

        self.merge_canvas.create_text(
            400, 15,
            text=f"MERGE FRUIT   SCORE: {self.merge_score}",
            fill="#00ffff",
            font=("Arial", 18, "bold")
        )

        self.merge_canvas.create_text(
            45, 65, text="NEXT",
            fill="white", font=("Arial", 10, "bold")
        )

        self.merge_draw_fruit(
            45, 100,
            self.merge_next_level, 13
        )

        if self.merge_running:
            self.merge_draw_fruit(
                self.merge_active_x,
                self.merge_active_y,
                self.merge_active_level,
                self.merge_sizes[self.merge_active_level]
            )

        for x, y, level in self.merge_fruits:
            self.merge_draw_fruit(
                x, y, level, self.merge_sizes[level]
            )

        self.merge_canvas.create_text(
            400, 550,
            text="LEFT / RIGHT = MOVE    SPACE = DROP    ESC = HOME",
            fill="white",
            font=("Arial", 12, "bold")
        )

        if not self.merge_running:
            self.merge_canvas.create_text(
                400, 270,
                text="GAME OVER!",
                fill="#ff3355",
                font=("Arial", 40, "bold")
            )

            self.merge_canvas.create_text(
                400, 315,
                text=f"Score: {self.merge_score}",
                fill="white",
                font=("Arial", 20, "bold")
            )

            tk.Button(
                self.root,
                text="PLAY AGAIN",
                command=self.merge_fruit_game,
                font=("Arial", 12, "bold")
            ).pack(pady=4)

            tk.Button(
                self.root,
                text="BACK",
                command=self.show_home,
                font=("Arial", 12, "bold")
            ).pack()

    def merge_draw_fruit(self, x, y, level, size):
        self.merge_canvas.create_oval(
            x - size, y - size,
            x + size, y + size,
            fill=self.merge_colors[level],
            outline="white",
            width=2
        )

        self.merge_canvas.create_text(
            x, y,
            text=self.merge_names[level],
            fill="white",
            font=("Arial", max(10, size // 2), "bold")
        )

    def merge_fruit_game(self):
        self.clear()

        self.merge_canvas = tk.Canvas(
            self.root, width=800, height=560,
            bg="#10101c", highlightthickness=0
        )
        self.merge_canvas.pack()
        self.merge_canvas.focus_set()

        self.merge_running = True
        self.merge_score = 0
        self.merge_fruits = []
        self.merge_next = random.randint(0, 2)
        self.merge_x = 400
        self.merge_y = 80
        self.merge_falling = True

        self.merge_names = ["🍒", "🍓", "🍊", "🍎", "🍐", "🍉"]
        self.merge_sizes = [18, 23, 29, 36, 44, 53]
        self.merge_colors = [
            "#ff3355", "#ff6699", "#ff9900",
            "#ff3333", "#99cc33", "#33cc66"
        ]

        self.merge_canvas.bind("<Left>", lambda e: self.merge_move(-25))
        self.merge_canvas.bind("<Right>", lambda e: self.merge_move(25))
        self.merge_canvas.bind("<space>", lambda e: self.merge_drop())
        self.merge_canvas.bind("<Escape>", lambda e: self.show_home())

        self.merge_draw()
        self.merge_loop()

    def merge_move(self, amount):
        if self.merge_running and self.merge_falling:
            self.merge_x = max(130, min(670, self.merge_x + amount))
            self.merge_draw()

    def merge_drop(self):
        if not self.merge_running or not self.merge_falling:
            return

        self.merge_fruits.append([self.merge_x, 120, self.merge_next])
        self.merge_next = random.randint(0, 2)
        self.merge_x = 400
        self.merge_y = 80
        self.merge_falling = True

    def merge_loop(self):
        if not self.merge_running:
            self.merge_draw()
            return

        if self.merge_falling:
            self.merge_y += 7

            if self.merge_y >= 120:
                self.merge_fruits.append([self.merge_x, 120, self.merge_next])
                self.merge_next = random.randint(0, 2)
                self.merge_x = 400
                self.merge_y = 80
                self.merge_falling = True

        # Move every fruit down until it rests.
        self.merge_fruits.sort(key=lambda f: f[1])

        for i in range(len(self.merge_fruits)):
            x, y, level = self.merge_fruits[i]
            size = self.merge_sizes[level]
            target = 500

            for j in range(i):
                ox, oy, other = self.merge_fruits[j]
                other_size = self.merge_sizes[other]

                if abs(x - ox) < (size + other_size) * 0.75:
                    target = min(
                        target,
                        oy - (size + other_size) * 0.82
                    )

            if y > target:
                self.merge_fruits[i][1] = target

        # Merge matching fruits.
        merged = True
        while merged:
            merged = False

            for i in range(len(self.merge_fruits)):
                for j in range(i + 1, len(self.merge_fruits)):
                    x1, y1, l1 = self.merge_fruits[i]
                    x2, y2, l2 = self.merge_fruits[j]

                    distance = ((x1-x2)**2 + (y1-y2)**2) ** 0.5

                    if l1 == l2 and l1 < 5:
                        if distance < (self.merge_sizes[l1] * 1.5):
                            nx = (x1 + x2) / 2
                            ny = min(y1, y2)

                            self.merge_fruits.pop(j)
                            self.merge_fruits.pop(i)
                            self.merge_fruits.append([nx, ny, l1 + 1])

                            self.merge_score += (l1 + 1) * 10
                            merged = True
                            break

                if merged:
                    break

        # Game over when a fruit reaches the danger line.
        for x, y, level in self.merge_fruits:
            if y - self.merge_sizes[level] <= 145:
                self.merge_running = False
                break

        self.merge_draw()
        self.root.after(35, self.merge_loop)

    def merge_draw(self):
        self.merge_canvas.delete("all")

        self.merge_canvas.create_rectangle(
            90, 30, 710, 530,
            outline="#00ffff", width=3
        )

        self.merge_canvas.create_line(
            100, 145, 700, 145,
            fill="#ff3355", dash=(8, 8)
        )

        self.merge_canvas.create_text(
            400, 15,
            text=f"🍉 MERGE FRUIT    SCORE: {self.merge_score}",
            fill="#00ffff",
            font=("Arial", 18, "bold")
        )

        self.merge_canvas.create_text(
            45, 65, text="NEXT",
            fill="white", font=("Arial", 10, "bold")
        )
        self.merge_draw_fruit(45, 100, self.merge_next, 13)

        if self.merge_running and self.merge_falling:
            self.merge_draw_fruit(
                self.merge_x, self.merge_y,
                self.merge_next,
                self.merge_sizes[self.merge_next]
            )

        for x, y, level in self.merge_fruits:
            self.merge_draw_fruit(
                x, y, level, self.merge_sizes[level]
            )

        self.merge_canvas.create_text(
            400, 550,
            text="← → MOVE    SPACE = DROP    ESC = HOME",
            fill="white", font=("Arial", 12, "bold")
        )

        if not self.merge_running:
            self.merge_canvas.create_text(
                400, 270,
                text="GAME OVER!",
                fill="#ff3355",
                font=("Arial", 40, "bold")
            )
            self.merge_canvas.create_text(
                400, 315,
                text=f"Score: {self.merge_score}",
                fill="white", font=("Arial", 20, "bold")
            )

            tk.Button(
                self.root, text="PLAY AGAIN",
                command=self.merge_fruit_game,
                font=("Arial", 12, "bold")
            ).pack(pady=4)

            tk.Button(
                self.root, text="BACK",
                command=self.show_home,
                font=("Arial", 12, "bold")
            ).pack()

    def merge_draw_fruit(self, x, y, level, size):
        self.merge_canvas.create_oval(
            x - size, y - size,
            x + size, y + size,
            fill=self.merge_colors[level],
            outline="white",
            width=2
        )
        self.merge_canvas.create_text(
            x, y,
            text=self.merge_names[level],
            font=("Arial", max(10, size // 2))
        )

    # =====================================================
    # CYBER DODGE

    def cyber_dodge_game(self):
        self.clear()
        self.title("⚡ CYBER DODGE")

        canvas = tk.Canvas(self.root, width=760, height=450, bg="#050510", highlightthickness=2, highlightbackground="#00ffff")
        canvas.pack(pady=5)

        info = tk.Label(self.root, text="Move: ← → or A/D   •   Dodge the falling blocks!", font=("Arial", 12, "bold"), fg="white", bg="#080812")
        info.pack(pady=4)

        player = canvas.create_rectangle(365, 400, 395, 430, fill="#00ffff", outline="white", width=2)
        score = 0
        speed = 5
        running = True
        obstacles = []
        coins = []

        score_text = canvas.create_text(90, 30, text="Score: 0", fill="white", font=("Arial", 18, "bold"))
        best_text = canvas.create_text(670, 30, text="BEST: 0", fill="#00ffff", font=("Arial", 18, "bold"))
        best = 0

        keys = {"left": False, "right": False}

        def key_down(event):
            k = event.keysym.lower()
            if k in ("left", "a"):
                keys["left"] = True
            if k in ("right", "d"):
                keys["right"] = True

        def key_up(event):
            k = event.keysym.lower()
            if k in ("left", "a"):
                keys["left"] = False
            if k in ("right", "d"):
                keys["right"] = False

        def hit(a, b):
            ax1, ay1, ax2, ay2 = canvas.coords(a)
            bx1, by1, bx2, by2 = canvas.coords(b)
            return ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1

        def game_over():
            nonlocal running, best
            if not running:
                return
            running = False
            best = max(best, score)
            canvas.itemconfig(best_text, text=f"BEST: {best}")
            canvas.create_text(380, 210, text="GAME OVER", fill="white", font=("Arial", 34, "bold"), tags="over")
            canvas.create_text(380, 255, text=f"Score: {score}", fill="#00ffff", font=("Arial", 20, "bold"), tags="over")
            tk.Button(self.root, text="PLAY AGAIN", command=self.cyber_dodge_game, font=("Arial", 13, "bold"), bg="#15152b", fg="white", activebackground="#00ffff", activeforeground="black", relief="flat", padx=20, pady=8).pack(pady=5)

        def loop():
            nonlocal score, speed
            if not running:
                return

            if keys["left"]:
                canvas.move(player, -8, 0)
            if keys["right"]:
                canvas.move(player, 8, 0)

            px1, _, px2, _ = canvas.coords(player)
            if px1 < 5:
                canvas.move(player, 5 - px1, 0)
            if px2 > 755:
                canvas.move(player, 755 - px2, 0)

            if random.randint(1, 14) == 1:
                x = random.randint(10, 720)
                obstacle = canvas.create_rectangle(x, -30, x + random.randint(25, 55), 0, fill="#ff3355", outline="white")
                obstacles.append(obstacle)

            if random.randint(1, 45) == 1:
                x = random.randint(15, 735)
                coin = canvas.create_oval(x, -20, x + 18, -2, fill="#ffd700", outline="white")
                coins.append(coin)

            for obj in obstacles[:]:
                canvas.move(obj, 0, speed)
                if hit(player, obj):
                    game_over()
                    return
                if canvas.coords(obj)[1] > 450:
                    canvas.delete(obj)
                    obstacles.remove(obj)
                    score += 1

            for coin in coins[:]:
                canvas.move(coin, 0, speed)
                if hit(player, coin):
                    canvas.delete(coin)
                    coins.remove(coin)
                    score += 5
                elif canvas.coords(coin)[1] > 450:
                    canvas.delete(coin)
                    coins.remove(coin)

            speed = min(12, 5 + score // 15)
            canvas.itemconfig(score_text, text=f"Score: {score}")
            canvas.after(30, loop)

        self.root.bind("<KeyPress>", key_down)
        self.root.bind("<KeyRelease>", key_up)
        canvas.focus_set()
        self.back_button()
        loop()

    # WEBSITE LINKER
    # =====================================================

    def memory_match_game(self):
        self.clear()
        self.title("🧠 MEMORY MATCH")
        self.memory_buttons=[]
        self.memory_first=None
        self.memory_locked=False
        self.memory_symbols=list("AABBCCDDEEFF")
        random.shuffle(self.memory_symbols)
        frame=tk.Frame(self.root,bg="#080812")
        frame.pack()
        for i in range(12):
            b=tk.Button(frame,text="?",font=("Arial",18,"bold"),width=5,height=2,
                         command=lambda i=i:self.memory_flip(i))
            b.grid(row=i//4,column=i%4,padx=5,pady=5)
            self.memory_buttons.append(b)
        self.memory_status=tk.Label(self.root,text="Find all 6 pairs!",font=("Arial",15),fg="white",bg="#080812")
        self.memory_status.pack(pady=10)
        self.back_button()

    def memory_flip(self,i):
        if self.memory_locked or self.memory_buttons[i]["text"] != "?": return
        self.memory_buttons[i]["text"]=self.memory_symbols[i]
        if self.memory_first is None:
            self.memory_first=i
            return
        first=self.memory_first
        self.memory_first=None
        if self.memory_symbols[first] == self.memory_symbols[i]:
            self.memory_status.config(text="MATCH! 🎉")
        else:
            self.memory_locked=True
            self.memory_status.config(text="Try again!")
            self.root.after(700,lambda:self.memory_hide(first,i))

    def memory_hide(self,a,b):
        if not self.memory_buttons: return
        try:
            self.memory_buttons[a]["text"]="?"
            self.memory_buttons[b]["text"]="?"
            self.memory_locked=False
        except tk.TclError: pass

    def space_blaster_game(self):
        self.clear()
        self.title("🚀 SPACE BLASTER")
        self.space_canvas=tk.Canvas(self.root,width=700,height=430,bg="black",highlightthickness=0)
        self.space_canvas.pack()
        self.space_player=[350,380]
        self.space_bullets=[]
        self.space_enemies=[]
        self.space_score=0
        self.space_game=True
        self.space_canvas.create_text(60,20,text="Score: 0",fill="white",font=("Arial",14),tag="score")
        self.space_canvas.bind("<Left>",lambda e:self.space_move(-25))
        self.space_canvas.bind("<Right>",lambda e:self.space_move(25))
        self.space_canvas.bind("<space>",lambda e:self.space_shoot())
        self.space_canvas.focus_set()
        self.space_spawn_enemy()
        self.space_loop()
        self.back_button()

    def space_move(self,d):
        if self.space_game:
            self.space_player[0]=max(20,min(680,self.space_player[0]+d))

    def space_shoot(self):
        if self.space_game: self.space_bullets.append([self.space_player[0],355])

    def space_spawn_enemy(self):
        if getattr(self,"space_game",False):
            self.space_enemies.append([random.randint(20,680),45])
            self.root.after(900,self.space_spawn_enemy)

    def space_loop(self):
        if not getattr(self,"space_game",False): return
        c=self.space_canvas; c.delete("all")
        c.create_text(60,20,text=f"Score: {self.space_score}",fill="white",font=("Arial",14))
        c.create_text(self.space_player[0],380,text="🚀",font=("Arial",24))
        for b in self.space_bullets: b[1]-=12
        for e in self.space_enemies: e[1]+=5
        for b in self.space_bullets[:]:
            if b[1]<0: self.space_bullets.remove(b); continue
            c.create_oval(b[0]-3,b[1]-8,b[0]+3,b[1]+8,fill="cyan",outline="")
        for e in self.space_enemies[:]:
            c.create_text(e[0],e[1],text="👾",font=("Arial",22))
            if e[1]>410:
                self.space_game=False; c.create_text(350,210,text="GAME OVER",fill="red",font=("Arial",30,"bold")); return
        for b in self.space_bullets[:]:
            for e in self.space_enemies[:]:
                if abs(b[0]-e[0])<25 and abs(b[1]-e[1])<25:
                    if b in self.space_bullets: self.space_bullets.remove(b)
                    if e in self.space_enemies: self.space_enemies.remove(e)
                    self.space_score+=1
                    break
        self.root.after(40,self.space_loop)

    def brick_breaker_game(self):
        self.clear()
        self.title("🧱 BRICK BREAKER")
        tk.Label(self.root,text="Move with mouse or ← →",fg="white",bg="#080812",font=("Arial",12)).pack()
        self.bb=tk.Canvas(self.root,width=700,height=430,bg="black",highlightthickness=0)
        self.bb.pack()
        self.bb_p=[350,400]; self.bb_ball=[350,300,4,-4]; self.bb_score=0; self.bb_running=True
        self.bb_bricks=[[80+x*80,60+y*25] for y in range(4) for x in range(7)]
        self.bb.bind("<Motion>",self.bb_mouse); self.root.bind("<Left>", lambda e:self.bb_move(-30)); self.root.bind("<Right>", lambda e:self.bb_move(30))
        self.brick_loop(); self.back_button()

    def bb_mouse(self,e): self.bb_p[0]=max(50,min(650,e.x))

    def bb_move(self,d):
        if getattr(self,"bb_running",False): self.bb_p[0]=max(50,min(650,self.bb_p[0]+d))

    def brick_loop(self):
        if not getattr(self,"bb_running",False): return
        c=self.bb; c.delete("all")
        x,y,vx,vy=self.bb_ball; x+=vx; y+=vy
        if x<8 or x>692: vx=-vx
        if y<8: vy=-vy
        if y>385 and abs(x-self.bb_p[0])<65 and vy>0: vy=-abs(vy)
        for brick in self.bb_bricks[:]:
            bx,by=brick
            if abs(x-bx)<38 and abs(y-by)<12:
                self.bb_bricks.remove(brick); vy=-vy; self.bb_score+=1; break
        if y>430:
            self.bb_running=False; c.create_text(350,210,text="GAME OVER",fill="red",font=("Arial",30,"bold")); return
        self.bb_ball=[x,y,vx,vy]
        for bx,by in self.bb_bricks: c.create_rectangle(bx-35,by-10,bx+35,by+10,outline="cyan")
        c.create_rectangle(self.bb_p[0]-60,395,self.bb_p[0]+60,410,fill="white")
        c.create_oval(x-7,y-7,x+7,y+7,fill="white")
        c.create_text(55,20,text=f"Score: {self.bb_score}",fill="white",font=("Arial",14))
        self.root.after(25,self.brick_loop)

    def jump_dash_game(self):
        self.clear(); self.title("🦘 JUMP DASH")
        tk.Label(self.root,text="Press SPACE to jump",fg="white",bg="#080812",font=("Arial",12)).pack()
        self.jd=tk.Canvas(self.root,width=700,height=400,bg="#101020",highlightthickness=0); self.jd.pack()
        self.jd_player=[100,330,0]; self.jd_obstacles=[[650,350]]; self.jd_score=0; self.jd_running=True
        self.root.bind("<space>",lambda e:self.jd_jump()); self.jd_loop(); self.back_button()

    def jd_jump(self):
        if self.jd_running and self.jd_player[2]==0: self.jd_player[2]=-13

    def jd_loop(self):
        if not getattr(self,"jd_running",False): return
        c=self.jd; c.delete("all"); p=self.jd_player; p[2]+=1; p[1]+=p[2]
        if p[1]>=330: p[1]=330; p[2]=0
        for o in self.jd_obstacles: o[0]-=7
        if self.jd_obstacles[-1][0]<430: self.jd_obstacles.append([700,350])
        self.jd_obstacles=[o for o in self.jd_obstacles if o[0]>-30]
        for o in self.jd_obstacles:
            c.create_rectangle(o[0]-15,320,o[0]+15,350,fill="red")
            if abs(o[0]-p[0])<28 and p[1]>295: self.jd_running=False; c.create_text(350,190,text="GAME OVER",fill="red",font=("Arial",30,"bold")); return
        self.jd_score+=1
        c.create_rectangle(0,350,700,400,fill="#222244")
        c.create_text(p[0],p[1],text="🦘",font=("Arial",25)); c.create_text(55,20,text=f"Score: {self.jd_score//10}",fill="white",font=("Arial",14))
        self.root.after(35,self.jd_loop)

    def gem_catcher_game(self):
        self.clear(); self.title("💎 GEM CATCHER")
        tk.Label(self.root,text="Move with ← → and catch the gems",fg="white",bg="#080812",font=("Arial",12)).pack()
        self.gc=tk.Canvas(self.root,width=700,height=430,bg="black",highlightthickness=0); self.gc.pack()
        self.gc_player=350; self.gc_items=[]; self.gc_score=0; self.gc_running=True
        self.root.bind("<Left>",lambda e:self.gc_move(-25)); self.root.bind("<Right>",lambda e:self.gc_move(25))
        self.gc_spawn(); self.gc_loop(); self.back_button()

    def gc_move(self,d): self.gc_player=max(30,min(670,self.gc_player+d))

    def gc_spawn(self):
        if getattr(self,"gc_running",False): self.gc_items.append([random.randint(20,680),40,random.choice(["💎","⭐","☄️"]) ]); self.root.after(600,self.gc_spawn)

    def gc_loop(self):
        if not getattr(self,"gc_running",False): return
        c=self.gc; c.delete("all")
        for item in self.gc_items[:]:
            item[1]+=6; c.create_text(item[0],item[1],text=item[2],font=("Arial",20))
            if item[1]>390:
                if abs(item[0]-self.gc_player)<45: self.gc_score+=1; self.gc_items.remove(item)
                else: self.gc_items.remove(item)
        c.create_rectangle(self.gc_player-45,395,self.gc_player+45,410,fill="white")
        c.create_text(60,20,text=f"Gems: {self.gc_score}",fill="white",font=("Arial",14))
        self.root.after(40,self.gc_loop)

    def linker_game(self):
        self.clear()
        self.title("🔗 WEBSITE LINKER")

        tk.Label(
            self.root,
            text="Type a website or search",
            font=("Arial", 15),
            fg="white",
            bg="#080812"
        ).pack(pady=10)

        self.link_entry = tk.Entry(
            self.root,
            font=("Arial", 17),
            width=35
        )
        self.link_entry.pack(pady=10)

        self.link_entry.focus()

        self.button(
            "🌐 OPEN",
            self.open_website
        )

        tk.Label(
            self.root,
            text="Examples: google.com\nYouTube.com\nwikipedia.org",
            font=("Arial", 12),
            fg="#777799",
            bg="#080812"
        ).pack(pady=15)

        self.back_button()

    def open_website(self):
        text = self.link_entry.get().strip()

        if not text:
            return

        if "." in text and " " not in text:
            if not text.startswith("http://") and not text.startswith("https://"):
                text = "https://" + text
        else:
            text = "https://www.google.com/search?q=" + text.replace(" ", "+")

        webbrowser.open(text)


# =========================================================
# START
# =========================================================

root = tk.Tk()
app = MegaArcade(root)
root.mainloop()