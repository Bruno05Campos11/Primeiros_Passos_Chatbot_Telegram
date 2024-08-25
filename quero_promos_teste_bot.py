import telebot
from modulo_chave_api import RetornarChave

chave_api = RetornarChave()
bot = telebot.TeleBot (chave_api)

#----------------------------------------------------------------------------
menu = """
Clique em uma das opções abaixo:
/imprimir - Imprime as informações de sua mensagem no cmd
/nome - Veja que sei o seu nome
"""

#----------------------------------------------------------------------------
@bot.message_handler (commands=["salve"])

def ResponderSalve (mensagem):
	bot.reply_to (mensagem, "salve mano")

#----------------------------------------------------------------------------
def VerificarMensagem(mensagem):
	if mensagem.text == "como vc tá?":
		return True
	else:
		return False

@bot.message_handler (func=VerificarMensagem)

def ResponderToBem (mensagem):
	bot.reply_to (mensagem, "tô bem, e vc?")

#----------------------------------------------------------------------------
@bot.message_handler (commands=["imprimir"])

def ImprimirInformacoes (mensagem):
	print (mensagem)
	bot.send_message (mensagem.chat.id, "imprimi as informações da sua mensagem")

#----------------------------------------------------------------------------
@bot.message_handler(commands=["nome"])

def DescobrirNome (mensagem):
	enviar = "seu nome é " + mensagem.chat.first_name
	bot.send_message (mensagem.chat.id, enviar)

#----------------------------------------------------------------------------
def QualquerMensagem(mensagem):
		return True

@bot.message_handler (func=QualquerMensagem)

def ResponderMenu (mensagem):
	enviar = "Não tenho resposta para isso, confira meus comandos no menu\n" +menu
	bot.reply_to (mensagem, enviar)

#----------------------------------------------------------------------------

bot.polling()