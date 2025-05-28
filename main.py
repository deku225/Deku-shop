import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username or update.effective_user.first_name or "utilisateur"
    welcome_message = f"""
Deku Décryptor 🧩
Bienvenue {username} ! 👋

Voici les options disponibles :
"""
    keyboard = [
        [InlineKeyboardButton("🛍️ Produits", callback_data='produits')],
        [InlineKeyboardButton("🛒 Commander", callback_data='commander')],
        [InlineKeyboardButton("💬 Avis", callback_data='avis')],
        [InlineKeyboardButton("📞 Contacter un agent", callback_data='contact')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

# Callback placeholder
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    response_map = {
        'produits': "📦 *Produits disponibles :*
1. VPN Premium
2. Iptv
3. Décryptage HAT...",
        'commander': "🧾 Pour commander, choisissez votre mode de paiement :

*Orange:* +225 0718623773
*MTN:* +225 0575719113
*Wave:* +225 0596430369

Envoyez l'ID de la transaction ici et vous recevrez le lien de contact : [@deku225](https://t.me/deku225)",
        'avis': "💬 Merci de nous laisser un avis ici ! Votre retour compte pour nous.",
        'contact': "📞 Contactez un agent ici : [@deku225](https://t.me/deku225)"
    }
    await query.edit_message_text(response_map.get(query.data, "Option non reconnue."), parse_mode="Markdown")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_callback))

if __name__ == "__main__":
    app.run_polling()