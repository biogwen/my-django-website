from django.core.mail import EmailMessage


def mailing(sender, subject, message):


    email = EmailMessage(
        subject,
        message,
        sender,
        ['gwenael@mycoachingcompany.eu'],

        reply_to=[sender],
        headers={'Message-ID': 'site perso'},
    )
    email.send(fail_silently=False)
