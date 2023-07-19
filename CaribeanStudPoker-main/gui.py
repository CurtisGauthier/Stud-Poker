import tkinter as tk
import tkinter.font as TkFont
from cards import *
from PIL import ImageTk, Image

CURRENT_MODULE = __import__(__name__)

class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Fonts and Colours
        self.PAYOUT_FONT = TkFont.Font(family="Times New Roman",size=16,weight="bold")
        self.INPUT_FONT = TkFont.Font(family="Times New Roman",size=14)
        self.LOG_FONT = TkFont.Font(family="Times New Roman",size=8, weight="bold")
        self.POKER_GREEN = "#35654d"
        self.DARK_GREY = "#252525"
        
        # Define 
        self.resizable(False, False)
        self.title("Caribean Stud Poker")
        self.configure(bg=self.POKER_GREEN)

        # Window size
        self.w_height = self.winfo_screenheight()
        self.w_width = self.winfo_screenwidth()

        # Define minimum height of screen
        if self.w_height < 800 or self.w_width < 1400: 
            self.w_height = 800
            self.w_width = 1400

        self.geometry(f"{self.w_width}x{self.w_height}")

        # Initialize Full Frame
        self.fullFrame = tk.Frame(self, bg=self.POKER_GREEN, width=self.w_width, height=self.w_height)
        self.fullFrame.pack()
        
        # Variables
        self.card_height = int(0.21*self.w_height)
        self.card_width = int(0.08*self.w_width)
        self.dealer_hand_labels = []
        self.player_hand_labels = []
        self.buttons = []

        # Initialize GUI
        self.initializeMainFrame()
        self.initializeCards()
        self.initializeBottomButtons()
        self.initializeLogBox()
        self.initializeMoneyFrame()
        self.initializeAnteBet()
        self.initializeRaiseLabel()
        self.initializeBonusBet()
        self.initializePayoutFrame()
        self.initializeExitButton()
        self.initializeTitleScreen()

    # Initialize Functions
    def initializeMainFrame(self):
        # Initialize top frames
        self.money_frame = tk.Frame(self.fullFrame, bg=self.POKER_GREEN, width=0.25*self.w_width, height=0.15*self.w_height)
        self.title_frame = tk.Frame(self.fullFrame, bg=self.POKER_GREEN, width=0.5*self.w_width, height=0.15*self.w_height)
        self.exit_frame = tk.Frame(self.fullFrame, bg=self.POKER_GREEN, width=0.25*self.w_width, height=0.15*self.w_height)
        self.money_frame.grid(row=0, column=0)
        self.title_frame.grid(row=0, column=1)
        self.exit_frame.grid(row=0, column=2)

        # Initialize middle frames
        self.odds_frame = tk.Frame(self.fullFrame, bg=self.POKER_GREEN, width=0.25*self.w_width, height=0.85*self.w_height)
        self.log_frame = tk.Frame(self.fullFrame, bg=self.POKER_GREEN, width=0.25*self.w_width, height=0.85*self.w_height)
        self.middle_frame = tk.Frame(self.fullFrame, bg=self.POKER_GREEN, width=0.5*self.w_width, height=0.85*self.w_height)
        self.odds_frame.grid(row=1, column=0)
        self.middle_frame.grid(row=1, column=1)
        self.log_frame.grid(row=1, column=2)

        # Initialize middle middle frames
        self.dealer_frame = tk.Frame(self.middle_frame, bg=self.POKER_GREEN, width=0.5*self.w_width, height=0.25*self.w_height, highlightbackground="yellow", highlightthickness=2)
        self.player_frame = tk.Frame(self.middle_frame, bg=self.POKER_GREEN, width=0.5*self.w_width, height=0.25*self.w_height, highlightbackground="yellow", highlightthickness=2)
        self.button_frame = tk.Frame(self.middle_frame, bg=self.POKER_GREEN, width=0.5*self.w_width, height=0.15*self.w_height)
        self.bet_frame = tk.Frame(self.middle_frame, bg=self.POKER_GREEN, width=0.5*self.w_width, height=0.20*self.w_height)

        self.dealer_frame.grid(row=1, column=0)
        self.bet_frame.grid(row=2, column=0)
        self.player_frame.grid(row=3, column=0)
        self.button_frame.grid(row=4, column=0)

        # Disable propogate
        self.title_frame.grid_propagate(False)
        self.middle_frame.grid_propagate(False)
        self.money_frame.grid_propagate(False)
        self.odds_frame.grid_propagate(False)
        self.log_frame.grid_propagate(False)
        self.dealer_frame.grid_propagate(False)
        self.player_frame.grid_propagate(False)
        self.button_frame.grid_propagate(False)
        self.bet_frame.grid_propagate(False)
        self.exit_frame.grid_propagate(False)

    def initializeCards(self):
        for i in range(5):
            blank_card = ImageTk.PhotoImage(Image.open("images/cards/back_card.png").resize((self.card_width, self.card_height)))

            # Initiliaze dealer cards
            d_card_frame = tk.Frame(self.dealer_frame, bg=self.POKER_GREEN, width=self.card_width, height=self.card_height)
            d_card_frame.propagate(0)
            d_card_frame.grid(row=0, column=i, padx=(0.01*self.w_width), pady=(0.02*self.w_height))
            d_card_label = tk.Label(d_card_frame, bg=self.POKER_GREEN)
            d_card_label.configure(image=blank_card)
            d_card_label.image = blank_card
            d_card_label.pack()
            self.dealer_hand_labels.append(d_card_label)

            # Initiliaze player cards
            p_card_frame = tk.Frame(self.player_frame, bg=self.POKER_GREEN, width=self.card_width, height=self.card_height)
            p_card_frame.propagate(0)
            p_card_frame.grid(row=0, column=i, padx=(0.01*self.w_width), pady=(0.02*self.w_height))
            p_card_label = tk.Label(p_card_frame, bg=self.POKER_GREEN)
            p_card_label.configure(image=blank_card)
            p_card_label.image = blank_card
            p_card_label.pack()
            self.player_hand_labels.append(p_card_label)

    def initializeBottomButtons(self):
        for i in range(3):
            bf = tk.Frame(self.button_frame, bg='blue', width=0.14*self.w_width, height=0.05*self.w_height)
            bf.propagate(0)
            bf.grid(row=0, column=i, padx=(0.02*self.w_width,0), pady=(0.02*self.w_height, 0))
            
            button_width = int(0.14*self.w_width)
            button_height = int(0.05*self.w_height)
            if i == 0:
                new_image = ImageTk.PhotoImage(Image.open("images/misc/deal_button.png").resize((button_width, button_height)))
            elif i==1:
                new_image = ImageTk.PhotoImage(Image.open("images/misc/raise_button.png").resize((button_width, button_height)))
            else:
                new_image = ImageTk.PhotoImage(Image.open("images/misc/fold_button.png").resize((button_width, button_height)))

            new_button = tk.Button(bf, bg=self.POKER_GREEN)
            new_button.configure(image=new_image)
            new_button.image = new_image
            new_button.pack()

            new_button.pack(fill=tk.BOTH, expand=True)
            self.buttons.append(new_button)

    def initializeLogBox(self):
        log_frame_inner = tk.Frame(self.log_frame, bg=self.POKER_GREEN, width=0.2*self.w_width, height=0.80*self.w_height)
        log_frame_inner.grid(row=0, column=0, padx=(0.025*self.w_width))
        log_frame_inner.propagate(0)

        info_label = tk.Label(log_frame_inner, bg=self.POKER_GREEN, fg='yellow', font=self.PAYOUT_FONT, text='Output', justify=tk.LEFT)
        info_label.pack(anchor=tk.W)

        self.log = tk.Listbox(log_frame_inner, bg=self.POKER_GREEN, height=100, font=self.LOG_FONT, fg='white', highlightbackground="yellow", highlightthickness=1)
        self.log.pack(fill=tk.BOTH)
        self.log.propagate(0)
        self.log.bindtags((self.log, self, "all"))

        v_log_scrollbar = tk.Scrollbar(self.log, orient=tk.VERTICAL, troughcolor=self.POKER_GREEN)
        v_log_scrollbar.pack(side=tk.RIGHT, fill = tk.Y)
        self.log.config(yscrollcommand = v_log_scrollbar.set)
        v_log_scrollbar.config(command = self.log.yview)

        h_log_scrollbar = tk.Scrollbar(self.log, orient=tk.HORIZONTAL, troughcolor=self.POKER_GREEN)
        h_log_scrollbar.pack(side=tk.BOTTOM, fill = tk.X)
        self.log.config(xscrollcommand = h_log_scrollbar.set)
        h_log_scrollbar.config(command = self.log.xview)
    
    def initializeMoneyFrame(self):
        money_label_frame = tk.Frame(self.money_frame, bg=self.DARK_GREY, width=0.2*self.w_width, height=0.045*self.w_height, highlightbackground="yellow", highlightthickness=1)
        money_label_frame.grid(row=0, column=0, padx=0.025*self.w_width, pady=(0.02*self.w_height, 0))
        money_label_frame.propagate(0)

        self.money_label = tk.Label(money_label_frame, justify=tk.RIGHT, fg='yellow', bg=self.DARK_GREY, font=self.PAYOUT_FONT)
        self.money_label.pack(expand=True, anchor=tk.E)

        deposit_frame = tk.Frame(self.money_frame, bg=self.POKER_GREEN, width=0.2*self.w_width, height=0.03*self.w_height)
        deposit_frame.grid(row=1, column=0, padx=0.025*self.w_width, pady=(0.02*self.w_height, 0))
        deposit_frame.propagate(0)

        money_deposit_button_frame = tk.Frame(deposit_frame, bg=self.POKER_GREEN, width=0.09*self.w_width, height=0.03*self.w_height)
        money_deposit_button_frame.grid(row=0, column=0, padx=(0,0.02*self.w_width))
        money_deposit_button_frame.propagate(0)
        
        money_deposit_entry_frame = tk.Frame(deposit_frame, bg=self.POKER_GREEN, width=0.09*self.w_width, height=0.03*self.w_height)
        money_deposit_entry_frame.grid(row=0, column=1)
        money_deposit_entry_frame.propagate(0)

        deposit_image = ImageTk.PhotoImage(Image.open("images/misc/deposit_button.png").resize((int(0.09*self.w_width), int(0.03*self.w_height))))
        self.updateMoneyButton = tk.Button(money_deposit_button_frame, bg=self.POKER_GREEN)
        self.updateMoneyButton.configure(image=deposit_image)
        self.updateMoneyButton.image = deposit_image
        self.updateMoneyButton.pack(fill=tk.BOTH, expand=True)

        self.updateMoneyBox = tk.Entry(money_deposit_entry_frame, font=self.INPUT_FONT, justify=tk.CENTER)
        self.updateMoneyBox.pack(fill=tk.BOTH, expand=True)
        
    def initializeAnteBet(self):
        image_size = int(0.1*self.w_height)

        ante_frame = tk.Frame(self.bet_frame, bg=self.POKER_GREEN, width=0.1*self.w_width, height=0.1*self.w_height)
        ante_frame.grid(row=0, column=0, padx=(0.05*self.w_width,0), pady=(0.02*self.w_height))
        ante_frame.propagate(0)

        ante_image = ImageTk.PhotoImage(Image.open("images/misc/ante.png").resize((image_size, image_size)))
        ante_label = tk.Label(ante_frame, height=image_size, width=image_size, bg=self.POKER_GREEN)
        ante_label.configure(image=ante_image)
        ante_label.image = ante_image
        ante_label.pack()

        ante_input_frame = tk.Frame(self.bet_frame, width=0.1*self.w_width, height=0.02*self.w_height)
        ante_input_frame.grid(row=1, column=0, padx=(0.05*self.w_width,0), pady=(0,0.02*self.w_height))
        ante_input_frame.propagate(0)
        self.ante_input = tk.Entry(ante_input_frame, justify=tk.CENTER, font=self.INPUT_FONT)
        self.ante_input.pack(fill=tk.BOTH, expand=True)
    
    def initializeRaiseLabel(self):
        image_size = int(0.1*self.w_height)

        play_frame = tk.Frame(self.bet_frame, bg=self.POKER_GREEN, width=0.1*self.w_width, height=0.1*self.w_height)
        play_frame.grid(row=0, column=1, padx=(0.05*self.w_width), pady=(0.02*self.w_height))
        play_frame.propagate(0)

        play_image = ImageTk.PhotoImage(Image.open("images/misc/raise.png").resize((image_size, image_size)))
        play_label = tk.Label(play_frame, height=image_size, width=image_size, bg=self.POKER_GREEN)
        play_label.configure(image=play_image)
        play_label.image = play_image
        play_label.pack()

        raise_frame = tk.Frame(self.bet_frame, width=0.1*self.w_width, height=0.02*self.w_height, highlightbackground="yellow", highlightthickness=1)
        raise_frame.grid(row=1, column=1, padx=(0.05*self.w_width), pady=(0,0.02*self.w_height))
        raise_frame.propagate(0)
        self.raise_label = tk.Label(raise_frame, justify=tk.CENTER, fg='yellow', bg=self.POKER_GREEN, font=self.INPUT_FONT)
        self.raise_label.pack(fill=tk.BOTH, expand=True)
    
    def initializeBonusBet(self):
        image_size = int(0.1*self.w_height)

        bonus_frame = tk.Frame(self.bet_frame, bg=self.POKER_GREEN, width=0.1*self.w_width, height=0.1*self.w_height)
        bonus_frame.grid(row=0, column=2, padx=(0,0.05*self.w_width), pady=(0.02*self.w_height))
        bonus_frame.propagate(0)

        bonus_image = ImageTk.PhotoImage(Image.open("images/misc/bonus.png").resize((image_size, image_size)))
        bonus_label = tk.Label(bonus_frame, height=image_size, width=image_size, bg=self.POKER_GREEN)
        bonus_label.configure(image=bonus_image)
        bonus_label.image = bonus_image
        bonus_label.pack()

        bonus_input_frame = tk.Frame(self.bet_frame, width=0.1*self.w_width, height=0.02*self.w_height)
        bonus_input_frame.grid(row=1, column=2, padx=(0,0.05*self.w_width), pady=(0,0.02*self.w_height))
        bonus_input_frame.propagate(0)
        self.bonus_input = tk.Entry(bonus_input_frame, justify=tk.CENTER, font=self.INPUT_FONT)
        self.bonus_input.pack(fill=tk.BOTH, expand=True)
    
    def initializePayoutFrame(self):
        payout_frame_inner = tk.Frame(self.odds_frame, bg=self.POKER_GREEN, width=0.2*self.w_width, height=0.80*self.w_height)
        payout_frame_inner.grid(row=0, column=0, padx=0.025*self.w_width)
        payout_frame_inner.columnconfigure(0, weight=1)
        payout_frame_inner.columnconfigure(1, weight=1)
        payout_frame_inner.grid_propagate(False)

        payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='yellow', font=self.PAYOUT_FONT, text='Payout', justify=tk.LEFT)
        payout.grid(row=0, column=0, sticky='w')

        royal_flush = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='Royal Flush', justify=tk.LEFT)
        royal_flush_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='100 to 1', justify=tk.RIGHT)
        royal_flush.grid(row=1, column=0, sticky='w')
        royal_flush_payout.grid(row=1, column=1, sticky='e')

        straight_flush = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='Straight Flush', justify=tk.LEFT)
        straight_flush_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='50 to 1', justify=tk.RIGHT)
        straight_flush.grid(row=2, column=0, sticky='w')
        straight_flush_payout.grid(row=2, column=1, sticky='e')

        fours = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='Four of a Kind', justify=tk.LEFT)
        fours_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='20 to 1', justify=tk.RIGHT)
        fours.grid(row=3, column=0, sticky='w')
        fours_payout.grid(row=3, column=1, sticky='e')

        fullhouse = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='Full House', justify=tk.LEFT)
        fullhouse_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='7 to 1', justify=tk.RIGHT)
        fullhouse.grid(row=4, column=0, sticky='w')
        fullhouse_payout.grid(row=4, column=1, sticky='e')

        flush = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='Flush', justify=tk.LEFT)
        flush_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='5 to 1', justify=tk.RIGHT)
        flush.grid(row=5, column=0, sticky='w')
        flush_payout.grid(row=5, column=1, sticky='e')

        straight = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='Straight', justify=tk.LEFT)
        straight_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='4 to 1', justify=tk.RIGHT)
        straight.grid(row=6, column=0, sticky='w')
        straight_payout.grid(row=6, column=1, sticky='e')

        threes = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='Three of a Kind', justify=tk.LEFT)
        threes_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='3 to 1', justify=tk.RIGHT)
        threes.grid(row=7, column=0, sticky='w')
        threes_payout.grid(row=7, column=1, sticky='e')

        twopair = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='Two Pair', justify=tk.LEFT)
        twopair_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='2 to 1', justify=tk.RIGHT)
        twopair.grid(row=8, column=0, sticky='w')
        twopair_payout.grid(row=8, column=1, sticky='e')

        allother = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='All Other', justify=tk.LEFT)
        allother_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='1 to 1', justify=tk.RIGHT)
        allother.grid(row=9, column=0, sticky='w')
        allother_payout.grid(row=9, column=1, sticky='e')

        payout_gap = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, font=self.PAYOUT_FONT, text='\n\n', justify=tk.LEFT)
        payout_gap.grid(row=10, column=0, sticky='w')

        # 5+1 Bonus
        bonus_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='yellow', font=self.PAYOUT_FONT, text='5+1 Bonus', justify=tk.LEFT)
        bonus_payout.grid(row=11, column=0, sticky='w')

        bonus_royal_flush = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='Royal Flush', justify=tk.LEFT)
        bonus_royal_flush_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='1000 to 1', justify=tk.RIGHT)
        bonus_royal_flush.grid(row=12, column=0, sticky='w')
        bonus_royal_flush_payout.grid(row=12, column=1, sticky='e')

        bonus_straight_flush = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='Straight Flush', justify=tk.LEFT)
        bonus_straight_flush_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='200 to 1', justify=tk.RIGHT)
        bonus_straight_flush.grid(row=13, column=0, sticky='w')
        bonus_straight_flush_payout.grid(row=13, column=1, sticky='e')

        bonus_fours = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='Four of a Kind', justify=tk.LEFT)
        bonus_fours_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='100 to 1', justify=tk.RIGHT)
        bonus_fours.grid(row=14, column=0, sticky='w')
        bonus_fours_payout.grid(row=14, column=1, sticky='e')

        bonus_fullhouse = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='Full House', justify=tk.LEFT)
        bonus_fullhouse_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='20 to 1', justify=tk.RIGHT)
        bonus_fullhouse.grid(row=15, column=0, sticky='w')
        bonus_fullhouse_payout.grid(row=15, column=1, sticky='e')

        bonus_flush = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='Flush', justify=tk.LEFT)
        bonus_flush_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='15 to 1', justify=tk.RIGHT)
        bonus_flush.grid(row=16, column=0, sticky='w')
        bonus_flush_payout.grid(row=16, column=1, sticky='e')

        bonus_straight = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='Straight', justify=tk.LEFT)
        bonus_straight_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='10 to 1', justify=tk.RIGHT)
        bonus_straight.grid(row=17, column=0, sticky='w')
        bonus_straight_payout.grid(row=17, column=1, sticky='e')

        bonus_threes = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='Three of a Kind', justify=tk.LEFT)
        bonus_threes_payout = tk.Label(payout_frame_inner, bg=self.POKER_GREEN, fg='white', font=self.PAYOUT_FONT, text='7 to 1', justify=tk.RIGHT)
        bonus_threes.grid(row=18, column=0, sticky='w')
        bonus_threes_payout.grid(row=18, column=1, sticky='e')
    
    def initializeExitButton(self):
        exit_button_frame = tk.Frame(self.exit_frame, bg=self.DARK_GREY, width=0.1*self.w_width, height=0.035*self.w_height)
        exit_button_frame.grid(row=0, column=0, padx=(0.125*self.w_width,0.025), pady=(0.02*self.w_height))
        exit_button_frame.propagate(0)
        
        cashout_image = ImageTk.PhotoImage(Image.open("images/misc/cashout.png").resize((int(0.1*self.w_width), int(0.035*self.w_height))))
        self.cashoutButton = tk.Button(exit_button_frame, bg=self.POKER_GREEN)
        self.cashoutButton.configure(image=cashout_image)
        self.cashoutButton.image = cashout_image
        self.cashoutButton.pack(fill=tk.BOTH, expand=True)

    def initializeTitleScreen(self):
        logo_title_frame = tk.Frame(self.title_frame, bg='blue', width=0.4*self.w_width, height=0.1*self.w_height)
        logo_title_frame.grid(row=0, column=0, padx=0.05*self.w_width, pady=(0,0.01*self.w_height))
        logo_title_frame.propagate(0)

        logo_image = ImageTk.PhotoImage(Image.open("images/misc/logo.png").resize((int(0.4*self.w_width), int(0.1*self.w_height))))
        logo = tk.Label(logo_title_frame, bg=self.POKER_GREEN)
        logo.configure(image=logo_image)
        logo.image = logo_image
        logo.pack(fill=tk.BOTH, expand=True)

        qualifies_frame = tk.Frame(self.title_frame, bg=self.POKER_GREEN, width=0.3*self.w_width, height=0.01*self.w_height)
        qualifies_frame.grid(row=1, column=0, padx=0.1*self.w_width)
        info_label = tk.Label(qualifies_frame, bg=self.POKER_GREEN, fg='yellow', text="Dealer qualifies with Ace King", font=self.PAYOUT_FONT)
        info_label.pack(fill=tk.BOTH, expand=True, anchor=tk.CENTER)

    # Update functions
    def clearDepositEntry(self):
        self.updateMoneyBox.delete(0, tk.END)

    def updateMoneyLabel(self, money):
        money_string = str(money)
        while len(money_string) < 9:
            money_string = "0" + money_string
            
        self.money_label.configure(text=f"${money_string}")
        self.update()

    def updateRaiseLabel(self, ante_value):
        if ante_value == '':
            self.raise_label.configure(text="") 
        else:
            self.raise_label.configure(text=f"{int(ante_value)}")
        self.update()

    def insertLogMessage(self, index, string_outcome):
        self.log.insert(index, string_outcome)

    def revealOneCard(self, card, index, player):
        if player == 'dealer':
            current_label = self.dealer_hand_labels[index]
        else:
            current_label = self.player_hand_labels[index]

        full_link = "images/cards/" + card.returnImageLink() + ".png"
        img = ImageTk.PhotoImage(Image.open(full_link).resize((self.card_width, self.card_height)))
        current_label.configure(image=img)
        current_label.image = img
        self.update()

    def resetCards(self):
        for i in range(5):
            current_label_1 = self.dealer_hand_labels[i]
            current_label_2 = self.player_hand_labels[i]
            full_link = "images/cards/back_card.png"
            img = ImageTk.PhotoImage(Image.open(full_link).resize((self.card_width, self.card_height)))
            current_label_1.configure(image=img)
            current_label_1.image = img
            current_label_2.configure(image=img)
            current_label_2.image = img
            self.update()

    # Getters
    def checkAnteValue(self):
        if self.ante_input.get().isdigit() and int(self.ante_input.get()) > 0: return True
        return False
    
    def check51BonusValue(self):
        if self.bonus_input.get().isdigit() or self.bonus_input.get() == '': return True
        return False

    def get51BonusValue(self):
        if self.bonus_input.get() == '': return 0
        return int(self.bonus_input.get())
    
    def getAnteValue(self):
        return int(self.ante_input.get())
    
    def getMoneyEntryValue(self):
        value = self.updateMoneyBox.get()
        if value.isdigit() and len(value) < 10 and int(value) > 0: return int(value)
        return None

    def getDealButton(self):
        return self.buttons[0]
    
    def getRebetButton(self):
        return self.buttons[1]
    
    def getFoldButton(self):
        return self.buttons[2]
    
    def getUpdateMoneyButton(self):
        return self.updateMoneyButton
    
    def getCashoutButton(self):
        return self.cashoutButton
    
    # Disable Functions
    def disableEntry(self):
        self.ante_input.configure(state=tk.DISABLED)
        self.updateMoneyBox.configure(state=tk.DISABLED)
        self.bonus_input.configure(state=tk.DISABLED)

    def disableDealButton(self):
        self.buttons[0]['state'] = tk.DISABLED

    def disableRebetButton(self):
        self.buttons[1]['state'] = tk.DISABLED

    def disableFoldButton(self):
        self.buttons[2]['state'] = tk.DISABLED

    def disableUpdateMoneyButton(self):
        self.updateMoneyButton['state'] = tk.DISABLED

    # Enable Functions
    def enableDealButton(self):
        self.buttons[0]['state'] = tk.NORMAL
    
    def enableRebetButton(self):
        self.buttons[1]['state'] = tk.NORMAL

    def enableFoldButton(self):
        self.buttons[2]['state'] = tk.NORMAL

    def enableUpdateMoneyButton(self):
        self.updateMoneyButton['state'] = tk.NORMAL

    def enableEntry(self):
        self.ante_input.configure(state=tk.NORMAL)
        self.updateMoneyBox.configure(state=tk.NORMAL)
        self.bonus_input.configure(state=tk.NORMAL)