import json

with open('met_artworks.json', 'r') as f:
    data = json.load(f)

painting_keywords = ['oil','canvas','panel','tempera','fresco','watercolor','gouache','pastel','ink','drawing','print','engraving','etching','lithograph']

exact = {
    "The Holy Family": "성가족",
    "The Annunciation": "수태고지",
    "The Adoration of the Shepherds": "목자들의 경배",
    "The Adoration of the Magi": "동방박사의 경배",
    "The Nativity": "예수 탄생",
    "The Crucifixion": "십자가 처형",
    "The Resurrection": "부활",
    "The Last Supper": "최후의 만찬",
    "The Dance Class": "무용 수업",
    "The Harvesters": "추수하는 사람들",
    "Sunflowers": "해바라기",
    "Irises": "붓꽃",
    "Cypresses": "사이프러스",
    "Olive Trees": "올리브 나무",
    "Bathers": "목욕하는 사람들",
    "Young Woman with a Water Pitcher": "물 주전자를 든 젊은 여인",
    "Woman Reading": "독서하는 여인",
    "The Milkmaid": "우유 따르는 여인",
    "The Geographer": "지리학자",
    "The Astronomer": "천문학자",
    "The Lacemaker": "레이스 짜는 여인",
    "Erasmus of Rotterdam": "로테르담의 에라스무스",
    "Aristotle with a Bust of Homer": "호메로스 흉상을 바라보는 아리스토텔레스",
    "Return of the Prodigal Son": "탕자의 귀환",
    "Steamboats in the Port of Rouen": "루앙 항구의 증기선",
    "First Steps, after Millet": "첫 걸음 (밀레 모작)",
    "Oleanders": "협죽도",
    "Self-Portrait": "자화상",
    "Self-Portrait with a Straw Hat": "밀짚모자를 쓴 자화상",
    "Portrait of a Woman": "여인 초상",
    "Portrait of a Man": "남자 초상",
    "Portrait of a Young Woman": "젊은 여인 초상",
    "Portrait of a Young Man": "젊은 남자 초상",
    "Portrait of a Gentleman": "신사 초상",
    "Portrait of a Lady": "귀부인 초상",
    "Portrait of an Old Man": "노인 초상",
    "Head of a Woman": "여인의 두상",
    "Head of a Man": "남자의 두상",
    "Still Life": "정물화",
    "Landscape": "풍경화",
    "The Lamentation": "애도",
    "The Entombment": "매장",
    "The Garden of the Tuileries on a Winter Afternoon": "겨울 오후의 튈르리 정원",
    "Wheat Field with Cypresses": "사이프러스가 있는 밀밭",
}

patch = {}
for item in data:
    medium = item.get("medium","").lower()
    if not any(k in medium for k in painting_keywords):
        continue
    title = item["title"].strip()
    if title in exact:
        patch[item["file"]] = exact[title]
    else:
        for key, val in exact.items():
            if title.startswith(key + ",") or title.startswith(key + " ("):
                patch[item["file"]] = val
                break

with open("title_ko_patch.json", "w", encoding="utf-8") as f:
    json.dump(patch, f, ensure_ascii=False, indent=2)

print("번역 완료:", len(patch), "개")
for k,v in list(patch.items())[:10]:
    print(" ", k, ":", v)
