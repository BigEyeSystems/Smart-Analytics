class I18N:
    _STRINGS = {
        'bot.default_text': {
            'ru': """""",
            'kk': """""",
            'en': """
    🎉 Добро пожаловать в Smart Analytics!

Smart Analytics — это ваш персональный помощник в мире криптовалют и фондового рынка. Получайте актуальные данные, анализируйте рынок и принимайте взвешенные решения.

🔍 Исследуйте рынок: Отслеживайте изменения цен, активность торгов и рост активов в реальном времени.

📈 Анализируйте данные: Используйте эксклюзивные аналитические инструменты для глубокого понимания рыночных тенденций.

💼 Подписка: Откройте доступ к расширенным функциям и получайте максимум полезной информации.

Удачи в ваших инвестициях и успешных сделок! 🚀
"""
        },
        'bot.error_message': {
            'ru': "",
            'kk': "",
            'en': "Sorry some trouble occurred! Please try again.",
        },
        'bot.success_message': {
            'ru': "",
            'kk': "",
            'en': "You have just get subscriber by ID: {referred_id}!",
        },
        'bot.help_message': {
            'ru': "",
            'kk': "",
            'en': """FAQ: How to Traid"""
        },
        'bot.invited_client_welcome_text': {
            'ru': "🎉Привет, {user_nickname}! ",
            'en': " 🎉Hello, {user_nickname}! "
        },
        'bot.client_welcome_text': {
            'ru': "🎉Привет, {user_nickname}! ",
            'en': " 🎉Hello, {user_nickname}! "
        },
        'bot.confirmation_text': {
            'ru': "Пожалуйста, подождите, пока наш администратор разрешит вам проверить наш продукт!",
            'kk': "",
            'en': "Please wait until our admin will allow you to check our product!",
        },
    }

    def get_string(self, key, lang = 'en') -> str:
        return self._STRINGS.get(key, {}).get(str(lang), f'[INVALID_TRANSLATION:{lang}:{key}]')


i18n = I18N()