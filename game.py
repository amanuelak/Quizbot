from SECRET import token
import nextcord, time
from nextcord import Interaction
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = '!', intents = intents)

@bot.event
async def on_ready():
    print("The bot is ready")  

class Play(nextcord.ui.View):
    def  __init__(self):
        super().__init__()
        self.value = None
    
    @nextcord.ui.button(label = "Play", style = nextcord.ButtonStyle.green)
    async def play(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.send("Welcome to the environmental game!" , ephemeral = True) #set to false for everyone to see
        #await interaction.send("$question") #set to false for everyone to see
        self.value  = True
        self.stop()

    @nextcord.ui.button(label = "Quit", style=nextcord.ButtonStyle.grey)
    async def quit(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.send("Game quitted", ephemeral = True)
        self.value = False
        self.stop()

class land1(nextcord.ui.View):
    def  __init__(self):
        super().__init__()
        self.value = None
    
    @nextcord.ui.button(label = "🐿️", style = nextcord.ButtonStyle.primary)
    async def squirrel(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value  = 'squirrel'
        self.stop()

    @nextcord.ui.button(label = "🗿", style=nextcord.ButtonStyle.primary)
    async def rock(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'rock'
        self.stop()

    #    which tree is better? i like the third 
    @nextcord.ui.button(label = "🌲", style=nextcord.ButtonStyle.primary)
    async def tree(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'tree'
        self.stop()

class land2(nextcord.ui.View):
    def  __init__(self):
        super().__init__()
        self.value = None
    
    @nextcord.ui.button(label = "🐬", style = nextcord.ButtonStyle.primary)
    async def dolphin(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value  = 'dolphin'
        self.stop()

    @nextcord.ui.button(label = "🦈", style=nextcord.ButtonStyle.primary)
    async def shark(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'shark'
        self.stop()

    #    which tree is better? i like the third 
    @nextcord.ui.button(label = "🌴", style=nextcord.ButtonStyle.primary)
    async def tree(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'tree'
        self.stop()

class land3(nextcord.ui.View):
    def  __init__(self):
        super().__init__()
        self.value = None
    
    @nextcord.ui.button(label = "🌵", style = nextcord.ButtonStyle.primary)
    async def cactus(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value  = 'cactus'
        self.stop()

    @nextcord.ui.button(label = "🐪", style=nextcord.ButtonStyle.primary)
    async def camel(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'camel'
        self.stop()

    @nextcord.ui.button(label = "☀️", style=nextcord.ButtonStyle.primary)
    async def sun(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'sun'
        self.stop()

class mcquiz1(nextcord.ui.View):
    def  __init__(self):
        super().__init__()
        self.value = None
    
    @nextcord.ui.button(label = "48%", style = nextcord.ButtonStyle.primary)
    async def one(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value  = 'wrong'
        self.stop()

    @nextcord.ui.button(label = "10%", style=nextcord.ButtonStyle.primary)
    async def two(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'right'
        self.stop()

    @nextcord.ui.button(label = "20%", style=nextcord.ButtonStyle.primary)
    async def three(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'wrong'
        self.stop()

class mcquiz2(nextcord.ui.View):
    def  __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label = "True", style=nextcord.ButtonStyle.primary)
    async def two(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'right'
        self.stop()

    @nextcord.ui.button(label = "False", style=nextcord.ButtonStyle.primary)
    async def three(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'wrong'
        self.stop()

class mcquiz3(nextcord.ui.View):
    def  __init__(self):
        super().__init__()
        self.value = None
    
    @nextcord.ui.button(label = "60, 000", style = nextcord.ButtonStyle.primary)
    async def one(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value  = 'wrong'
        self.stop()

    @nextcord.ui.button(label = "100, 000", style=nextcord.ButtonStyle.primary)
    async def two(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'wrong'
        self.stop()

    @nextcord.ui.button(label = "80, 000", style=nextcord.ButtonStyle.primary)
    async def three(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'right'
        self.stop()

class quizshark(nextcord.ui.View):
    def  __init__(self):
        super().__init__()
        self.value = None
    
    @nextcord.ui.button(label = "Climate Change", style = nextcord.ButtonStyle.primary)
    async def one(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value  = 'right'
        self.stop()

    @nextcord.ui.button(label = "Air pollution", style=nextcord.ButtonStyle.primary)
    async def two(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'wrong'
        self.stop()

    @nextcord.ui.button(label = "Rising temperatures", style=nextcord.ButtonStyle.primary)
    async def three(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'wrong'
        self.stop()

class quizsun(nextcord.ui.View):
    def  __init__(self):
        super().__init__()
        self.value = None
    
    @nextcord.ui.button(label = "Turning of items powered by electricity when not in use", style = nextcord.ButtonStyle.primary)
    async def one(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value  = 'wrong'
        self.stop()

    @nextcord.ui.button(label = "Recycling correctly and reducing food waste", style=nextcord.ButtonStyle.primary)
    async def two(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'wrong'
        self.stop()

    @nextcord.ui.button(label = "All of the above", style=nextcord.ButtonStyle.primary)
    async def three(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'right'
        self.stop()

@bot.command()
async def start(ctx):

    view = Play()
    #user = bot.get_user_info(member.display_name)
    await ctx.send("Click Play to start your environmental learning journey! ", view = view)

    await view.wait()

    if view.value is None:
        print("Timmed out!")

    elif view.value:
        await ctx.send("Your adventure begins")
        time.sleep(0.2)
        await ctx.send("ᕕ( ᐛ )ᕗ")
        time.sleep(0.2)
        await ctx.send(" . . . . . ᕕ( ᐛ )ᕗ")
        time.sleep(0.2)
        await ctx.send(" . . . . . . . . . . ᕕ( ᐛ )ᕗ")
        time.sleep(0.2)
        await ctx.send(f"Hello {ctx.author.name} Earthling...")
        time.sleep(1)
        await ctx.send(f"I see you're interested in our planet.")
        time.sleep(1)
        await ctx.send("We'll take you through a series of places where you'll learn more about our home and about environmental sustainability.")
        time.sleep(1)
        await ctx.send("Get to the end and something might be waiting for you~")
        time.sleep(1)
        await ctx.send("Have fun 😉")

        time.sleep(0.2)
        await ctx.send(" . . . . . . . . . . ᕕ( ᐛ )ᕗ")
        time.sleep(0.2)
        await ctx.send(" . . . . . ᕕ( ᐛ )ᕗ")
        time.sleep(0.2)
        await ctx.send("ᕕ( ᐛ )ᕗ")
        time.sleep(0.2)

        view = land1()
        await ctx.send("You've reached the land of trees and see a squirrel, a rock, and a tree. Click on one of the options and see where they take you.", view = view)
        await view.wait()

        if view.value == 'squirrel':
            view = mcquiz1()
            await ctx.send("You've encountered an environment quiz!")
            time.sleep(1)
            await ctx.send("Question 1: What percent of the world’s forest is in Canada?", view = view)
            await view.wait()

            if view.value == 'right':
                await ctx.send("Correct!")
                time.sleep(0.5)
                await ctx.send("10% percent of the world’s forest are in Canada. The forest ecosystem is vital to the variety of plants and animals that live within Canada.")

            else:
                await ctx.send("Whoops! That's not the right answer but that's okay. It's actually 10%.")
                time.sleep(0.5)
                await ctx.send("The forest ecosystem is vital to the variety of plants and animals that live within Canada.")

            time.sleep(1)
            view = mcquiz2()
            await ctx.send("Question 2: A 2°C increase globally means a 3 to 4ºC temperature increase for Canada", view = view)
            await view.wait()

            if view.value == 'right':
                await ctx.send("Correct! Environment and Climate change Canada (ECCC) has stated that increases in temperatures are caused mainly by human activities such as deforestation and greenhouse gas emissions.")

            else:
                await ctx.send("It's okay to get stuff wrong, as long as you learn from it.")
                time.sleep(0.5)
                await ctx.send("The answer is true. Environment and Climate change Canada (ECCC) has stated that increases in temperatures are caused mainly by human activities such as deforestation and greenhouse gas emissions.")

            time.sleep(1)
            view = mcquiz3()
            await ctx.send("Question 3: About ______ species are known to exist in Canada, excluding bacteria and viruses.", view = view)
            await view.wait()

            if view.value == 'right':
                await ctx.send("Correct!")
                time.sleep(0.5)
                await ctx.send("Correct! With Canada’s rich diversity of life, there are also many threats including habitat destruction, pollutions and overexplotation.")
                time.sleep(0.5)
                await ctx.send("See more information at https://www.canada.ca/en/environment-climate-change/services/environmental-indicators/status-wild-species.html")

            else:
                await ctx.send("The answer is actually 80, 000. Thanks for guessing!")
                time.sleep(0.5)
                await ctx.send("With Canada’s rich diversity of life, there are also many threats including habitat destruction, pollutions and overexplotation.")
                time.sleep(0.5)
                await ctx.send("See more information at https://www.canada.ca/en/environment-climate-change/services/environmental-indicators/status-wild-species.html")

        elif view.value == 'rock':
            await ctx.send("Sherlock, what type of rock is this amazing specimen?")
            time.sleep(1)
            await ctx.send(" . . . . .")
            time.sleep(0.5)
            await ctx.send(" . . . ")
            time.sleep(0.5)
            await ctx.send(" . ")
            time.sleep(0.5)
            await ctx.send("It’s *sedimentary*, my dear Watson.")

        elif view.value == 'tree':
            await ctx.send("Did you know that trees talk to each other using an internet of fungus?")
            time.sleep(1)
            await ctx.send("You’ll find them using the fungal network to share nutrients and information, or even sabotage unwelcome plants by spreading toxic chemicals through the network.")

        time.sleep(1)

        view = land2()
        await ctx.send("Let's explore another area!")
        time.sleep(0.2)
        await ctx.send("ᕕ( ᐛ )ᕗ")
        time.sleep(0.2)
        await ctx.send(" . . . . . ᕕ( ᐛ )ᕗ")
        time.sleep(0.2)
        await ctx.send(" . . . . . . . . . . ᕕ( ᐛ )ᕗ")

        await ctx.send("You've arrived at the beautiful ocean!")
        time.sleep(1)
        await ctx.send("Over there is a dolphin, a shark, and a palm tree. Clicking on one of them should take you somewhere.", view = view)
        await view.wait()

        if view.value == 'dolphin':
            await ctx.send("Underwater noise pollution is a threat to dolphins!")
            time.sleep(1)
            await ctx.send("Noise pollution from naval activity, the oil and gas industry, seismic surveys and underwater construction can stress and injure cetaceans.")
            time.sleep(1)
            await ctx.send("It also severely interferes with their ability to communicate, reproduce, navigate and find prey - sometimes proving fatal.")
        
        elif view.value == 'shark':
            view = quizshark()
            await ctx.send("What is the top environmental issue that is affecting Canada?", view = view)
            await view.wait()

            if view.value == 'right':
                await ctx.send("Correct!")
                time.sleep(0.5)
                await ctx.send("Climate change is the number one issue in Canada threatening its environment.")
                time.sleep(0.5)
                await ctx.send("Over the years, shifts in global temperatures have caused a shift in precipitation patterns, melting of ice caps and hazardous weather which is negatively impacting our ecosystems and our daily lives.")
                time.sleep(0.5)
                await ctx.send("Follow this link to see Canada’s plan in tackling climate change: https://www.canada.ca/en/services/environment/weather/climatechange/climate-plan/climate-plan-overview.html/")

            else:
                await ctx.send("Nice guess but the answer is actually climate change!")
                time.sleep(0.5)
                await ctx.send("Climate change is the number one issue in Canada threatening its environment.")
                time.sleep(0.5)
                await ctx.send("Over the years, shifts in global temperatures have caused a shift in precipitation patterns, melting of ice caps and hazardous weather which is negatively impacting our ecosystems and our daily lives.")
                time.sleep(0.5)
                await ctx.send("Follow this link to see Canada’s plan in tackling climate change: https://www.canada.ca/en/services/environment/weather/climatechange/climate-plan/climate-plan-overview.html/")

        elif view.value == 'tree':
            await ctx.send("What do you call a palm tree that wants to be a rapper?")
            time.sleep(1)
            await ctx.send("*Slim Shady* 😎")

        time.sleep(1)

        view = land3()
        await ctx.send("Finally, it's time for the last destination!")
        time.sleep(0.2)
        await ctx.send(" . . . . . . . . . . ᕕ( ᐛ )ᕗ")
        time.sleep(0.2)
        await ctx.send(" . . . . . ᕕ( ᐛ )ᕗ")
        time.sleep(0.2)
        await ctx.send("ᕕ( ᐛ )ᕗ")
        time.sleep(0.2)
        await ctx.send("You can feel the blazing heat of the desert and spot a cactus, a camel, and the sun. Selecting one of the objects should lead you to the finale.", view = view)
        await view.wait()

        if view.value == 'cactus':
            await ctx.send("I once knew a cactus that lived on Sesame Street.")
            time.sleep(1)
            await ctx.send("I used to call it *Prickle me Elmo*.")
        
        elif view.value == 'camel':
            await ctx.send("Did you know camels not only live in hot environments?")
            time.sleep(1)
            await ctx.send("They're adaptable to both the extreme cold and hot!")

        elif view.value == 'sun':
            view = quizsun()
            await ctx.send("What is a small change you can do in your daily life to help the environment?", view = view)
            await view.wait()

            if view.value == 'right':
                await ctx.send("Correct!")
                time.sleep(0.5)
                await ctx.send("All of the answers mentioned above are amazing ways you can positively impact your environment.")
                time.sleep(0.5)
                await ctx.send("Here are some other ways you can help the environment: https://www.canada.ca/en/environment-climate-change/services/climate-change/things-you-can-do-help-environment.html")

            else:
                await ctx.send("The answer is actually all of the above. Nice try!")
                time.sleep(0.5)
                await ctx.send("All of the answers mentioned above are amazing ways you can positively impact your environment.")
                time.sleep(0.5)
                await ctx.send("Here are some other ways you can help the environment: https://www.canada.ca/en/environment-climate-change/services/climate-change/things-you-can-do-help-environment.html")

        time.sleep(1)

        await ctx.send(f"Congrats {ctx.author.name} on making it to the end of your long journey!")
        time.sleep(1)
        await ctx.send("Here's a badge for your hard work!")
        time.sleep(1)
        await ctx.send(file=nextcord.File('badge.png'))
        time.sleep(1)
        await ctx.send("If you're up to the task want to try our bonus quiz?")
        time.sleep(1)
        await ctx.send("Type '$question' and try out our bonus 😉 ")

    else:
        print("Cancelled")

bot.run(token)

