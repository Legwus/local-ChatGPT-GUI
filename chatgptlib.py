# Make sure to have the openai library downloaded. You can do that using pip.
import openai
from tkinter import *

# Enter your OpenAI API Key here. You can get it from their website.
openai.api_key = "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"

# Choose your model engine. This will determine the language model that will process your input and generate a response.
# The following order is in terms of performance. The possibilities are text-davinci-003 or 002, text-curie-001, text-babbage-001 or text-ada-001
model_engine = "text-davinci-003"


root = Tk()

root.title ('OpenAi')

# If this icon thing doesn't work, try putting the openai.ico file into User/.vscode. The .vscode folder is hidden by default.
root.iconbitmap('openai.ico')

# Tweak this to your liking if you want to change the resolution of the window on startup.
root.geometry ('800x500')

# Breakline label. Maybe there is some way to create space between objects in tkinter, i was lazy tho, so that's that.
blLabel = Label(root, text = '')
blLabel.pack()

# This is the input bar. If you put nothing in, the ai will decide a question for you.
E = Entry(root, width= 70, bg = 'lightgray')
E.pack()


blLabel = Label(root, text = '')
blLabel.pack()

   
# The text box including a scrollbar attachment, for times when the conversation gets long.   

tekst = Text(root, wrap=WORD)
tekst.pack()


# actually no idea what this stuff does, ChatGPT told me to use this so i did.
# I presume yview means that the orientation is vertical (scrollbar goes up and down), and side=RIGHT seems pretty self explanatory.
Scrollbar = Scrollbar(root, command=tekst.yview)
Scrollbar.pack(side=RIGHT, fill=Y)

tekst.config(yscrollcommand=Scrollbar.set)
# This is the size of your text box. if you want it wider or higher, tweak this.
tekst.configure(width=60, height= 20)



# Main function that operates the button click.
def klik(): 
    # prompt is the input you give to ChatGPT. It is set to fetch the input you put into the input bar e.
    prompt = E.get()
    tekst.insert(END, 'Legwus said : ' + E.get() )

    # This deletes whatever you put into the input bar, so you don't have to delete it when you want to put a different input.

    E.delete(0, END)

    # OpenAI API config stuff. max_tokens means how many tokens ChatGPT can use for the response. From what i realized, 1 character = 1 token.
    # The total amount of tokens is calculated by adding your prompt and the generated response together. Apparently, simpler language models are cheaper to use.
    # n = How many completions to generate for each prompt.
    # stop = idfk, i didn't even understand the explanation they put on their website.
    # Temperature = the higher the number here, the more funky and quirky and creative ChatGPU gets. Ff you need a specific answer, go low, for creative go high.

    completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.7)
    message = completion.choices[0].text

    # This is what will appear as ChatGPT's response in the Textbox.
    tekst.insert(END, message + '\n \n \n' )
    tekst.see(END)

    




blLabel = Label(root, text = '')
blLabel.pack()

# This is the button that you click to generate responses.
botan = Button(root, text = 'Ask ChatGPT', padx = 10, pady = 10, command=klik)
botan.pack()



root.mainloop()


