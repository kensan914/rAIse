from chat.models import Pattern


def chat(request, message):
    p_flt = Pattern.objects.filter(user__username=request.user)
    for p in p_flt:
        if p.pattern_text in message:
            return p.output_text
    return 'ちょっと分かりません'
