# -*- coding: utf-8 -*-
"""Question-answering-BERT-model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PKWvZk_bZbaofOi2JkVfGQkLX_fy0buZ

**Install Dependencies**
"""

pip install transformers torch

"""**Import Necessary Libraries and Load Pre-Trained Model**"""

from transformers import DistilBertForQuestionAnswering, DistilBertTokenizer
import torch

# Load pre-trained model
model_name = 'distilbert-base-uncased-distilled-squad'
model = DistilBertForQuestionAnswering.from_pretrained(model_name)
tokenizer = DistilBertTokenizer.from_pretrained(model_name)

"""**Word Tokenization**"""

def answer_question(question, context, max_len=512):
    # Tokenize question
    question_tokens = tokenizer.tokenize(tokenizer.cls_token + question + tokenizer.sep_token)
    max_context_len = max_len - len(question_tokens) - 1

    # Split context into chunks
    context_tokens = tokenizer.tokenize(context)
    chunks = [context_tokens[i:i + max_context_len] for i in range(0, len(context_tokens), max_context_len)]

    best_answer = ""
    best_score = float('-inf')

    for chunk in chunks:
        # Prepare inputs
        input_tokens = question_tokens + chunk + [tokenizer.sep_token]
        input_ids = tokenizer.convert_tokens_to_ids(input_tokens)
        input_ids = torch.tensor([input_ids])

        # Get the model outputs
        with torch.no_grad():
            outputs = model(input_ids)

        # Extract the start and end scores for the answer
        answer_start_scores = outputs.start_logits
        answer_end_scores = outputs.end_logits

        # Find the tokens with the highest `start` and `end` scores
        answer_start = torch.argmax(answer_start_scores)
        answer_end = torch.argmax(answer_end_scores) + 1

        # Convert tokens to words
        answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[0][answer_start:answer_end]))
        score = answer_start_scores[0, answer_start].item() + answer_end_scores[0, answer_end-1].item()

        if score > best_score:
            best_score = score
            best_answer = answer

    return best_answer

"""**Mahabharata**"""

# Define a function to interact with the chatbot
def chat_with_bot():
    print("Welcome to the Mahabharata chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        else:
            # Provide a context
            context = """The Mahabharata tells the story of two sets of cousins, the Pandavas and the Kauravas, whose rivalry leads to a massive conflict. It begins with King Shantanu's marriage to Ganga, who gives birth to Bhishma. Bhishma's vow of celibacy sets the stage for the unfolding drama. The central conflict arises between the Pandavas, led by Yudhishthira, and the Kauravas, led by Duryodhana. The Pandavas face trials including exile and betrayal, while the Kauravas conspire against them.

The epic culminates in the great war of Kurukshetra, where the Pandavas, with Lord Krishna as their advisor, confront the Kauravas. This war represents a clash of righteousness and unrighteousness, with moral and spiritual dilemmas at its core. The Bhagavad Gita, delivered by Lord Krishna to Arjuna during the war, offers profound insights into duty and the nature of existence. Arjuna gains clarity and embraces his role as a warrior.

The Mahabharata concludes with the triumph of the Pandavas, establishing dharma and justice under Yudhishthira's rule. Despite the victory, it comes at a great cost, symbolizing the complexities of human nature and the consequences of conflict. The epic marks the beginning of a new era in Bharatavarsha's history, leaving behind a legacy of wisdom and moral teachings that continue to resonate through generations."""
            answer = answer_question(user_input, context)
            print("Chatbot:", answer)

# Start chatting with the bot
chat_with_bot()

"""**Ramayana**"""

# Define a function to interact with the chatbot
def chat_with_bot():
    print("Welcome to the Ramayana chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        else:
            # Provide a context
            context = """The rescue of Sita from the clutches of Ravana is one of the most dramatic and pivotal episodes in the Ramayana. Here's a detailed summary of how Rama, aided by Hanuman and his army of Vanaras, accomplished this formidable task:

1. **Hanuman's Journey to Lanka:**
   - After learning of Sita's abduction, Rama forms an alliance with Sugriva, the Vanara king, who promises to assist him in locating Sita.
   - Hanuman, the mighty and devoted Vanara warrior, volunteers to undertake the perilous mission of finding Sita.
   - Hanuman's leap across the ocean to reach Lanka is an extraordinary feat, symbolizing his strength, agility, and unwavering devotion to Rama.

2. **Discovery of Sita:**
   - Disguised as a diminutive creature, Hanuman stealthily enters Lanka and begins his search for Sita.
   - After overcoming various obstacles and adversaries, Hanuman locates Sita in the Ashoka grove, where she remains imprisoned and despondent, guarded by female demons.

3. **Hanuman's Encounter with Sita:**
   - Hanuman reveals his true form to Sita, assuring her of Rama's love and determination to rescue her.
   - He presents Rama's signet ring as a token of proof, instilling hope and courage in Sita's heart amid her despair and longing for Rama.

4. **Hanuman's Exploits in Lanka:**
   - Hanuman wreaks havoc in Lanka, displaying his prowess and resourcefulness by defeating Ravana's forces and causing widespread destruction.
   - He confronts Ravana's brother, Indrajit, in battle, but is ultimately captured and brought before Ravana.

5. **Hanuman's Audience with Ravana:**
   - In Ravana's court, Hanuman boldly declares his allegiance to Rama and warns Ravana of the dire consequences of his actions.
   - Despite Ravana's attempts to intimidate and subdue him, Hanuman remains steadfast and defiant, refusing to yield to Ravana's threats.

6. **Hanuman's Escape and Return to Rama:**
   - Hanuman uses his magical abilities to escape from captivity, setting Lanka ablaze as a display of his power and determination.
   - Returning to Rama, Hanuman recounts his adventures in Lanka and delivers Sita's message, reaffirming her unwavering faith in Rama's ability to rescue her.

7. **Preparation for War:**
   - Inspired by Hanuman's bravery and the news of Sita's whereabouts, Rama mobilizes his army, including Sugriva's Vanaras and an alliance of divine beings, in preparation for a decisive battle against Ravana.

8. **The Battle of Lanka:**
   - Rama, supported by Hanuman and his allies, engages Ravana and his demon forces in a fierce and protracted battle, fought with valor and determination on both sides.
   - The climactic showdown culminates in Rama's triumph over Ravana, leading to Sita's liberation and the restoration of righteousness and order.

The rescue of Sita from Lanka exemplifies the unwavering devotion, courage, and perseverance of Rama, Hanuman, and their allies in the face of seemingly insurmountable odds, reaffirming the triumph of good over evil in the epic saga of the Ramayana."""
            answer = answer_question(user_input, context)
            print("Chatbot:", answer)

# Start chatting with the bot
chat_with_bot()

"""**Romeo and Juliet :**
*Poem*
"""

# Define a function to interact with the chatbot
def chat_with_bot():
    print("Welcome to the Romeo and Juliet chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        else:
            # Provide a context
            context = """In the streets of Verona, where the sun sets,
Two families, equal in status,
Cast long shadows over a place where love could grow,
But their hatred keeps them apart.

Juliet, a Capulet, as beautiful as dawn,
Pure like a lily,
She unknowingly follows a path
Towards a sweet but tragic love.

Romeo, from the noble Montague family,
Has a heart full of youthful desire,
He sees Juliet, whose eyes shine like stars,
And feels a secret love for her.

Under the gentle light of the moon,
They whisper their vows in quiet gardens,
Their love is pure, even in the dark night,
But fate brings them trouble.

Their families' anger is like a wild storm,
It cannot be calmed by their love,
They are like children in the arms of passion,
Heading towards a cruel end.

With every kiss and sigh,
They come closer to their destiny,
Their wedding day is also a final goodbye,
A potion puts them to sleep forever.

In the tomb where lovers rest,
Romeo thinks Juliet is dead,
He drinks poison and kisses her for the last time,
His final words are spoken.

Juliet wakes up to see Romeo dead,
She finds him lifeless by her side,
She takes a dagger and joins him in death,
Together forever.

Two hearts, one love, a city in conflict,
From their graves, a lesson is learned,
Hate and love are closely connected,
And peace comes through their sacrifice.

In Verona, where the sun sets,
Two families, equal in status,
Remember the sad story,
Of star-crossed lovers' tragic unity."""
            answer = answer_question(user_input, context)
            print("Chatbot:", answer)

# Start chatting with the bot
chat_with_bot()

"""**Romeo and Juliet**

1.Where does the story of Romeo and Juliet take place?

2.What is the status of the two families in the poem?

3.How is Juliet described in the poem?

4.Which family does Romeo belong to?

5.Where do Romeo and Juliet whisper their vows?

6.What is the reaction of their families to Romeo and Juliet's love?

7.What event marks the final goodbye for Romeo and Juliet?

8.What lesson is learned from the tragic story of Romeo and Juliet according to the poem?

9.What does Romeo mistakenly believe about Juliet when he finds her in the tomb?

10.How does Juliet respond when she wakes up and finds Romeo dead?

**Ramayana questions**

1.How does Hanuman's journey to Lanka signify his loyalty to Rama and his commitment to rescuing Sita?

2.Where does Hanuman locate Sita?

3.What token of proof does Hanuman present to Sita to assure her of Rama's love and determination?

4.What does Hanuman do in Lanka to display his prowess and resourcefulness?

5.Who does Hanuman confront in battle while wreaking havoc in Lanka?

6.Who forms an alliance with Sugriva to assist in locating Sita?

7.Which Vanara warrior volunteers to undertake the perilous mission of finding Sita?

8.What symbolizes Hanuman's strength, agility, and unwavering devotion to Rama?

9.How does Hanuman disguise himself while searching for Sita in Lanka?

**Mahabharata questions**

1.Who are the central characters in the Mahabharata, and what familial relationship do they share?

2.What sets off the central conflict between the Pandavas and the Kauravas?

3.How does the conflict between the Pandavas and the Kauravas escalate to the infamous game of dice?

4.What pivotal event marks the climax of the Mahabharata narrative?

5.How does the Bhagavad Gita contribute to the moral and spiritual themes of the Mahabharata?

6.What role does Lord Krishna play in the epic, particularly during the war?

7.Reflect on the legacy and enduring relevance of the Mahabharata as a timeless epic and source of wisdom.
"""