def extract_feature_requests(text):
    feature_map = {
        "editar perfil": "EDITAR_PERFIL",
        "notificações personalizadas": "NOTIFICACOES_PERSONALIZADAS",
        "mais meditações": "MAIS_MEDITACOES"
    }

    features = []
    for phrase, code in feature_map.items():
        if phrase in text.lower():
            features.append({"code": code, "reason": f"O usuário solicitou {phrase}"})
    return features
