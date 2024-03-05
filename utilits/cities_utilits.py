from models import City


def response_to_command_info_city(city: City, info_the_city: dict) -> str:
    text = (f"Вы выбрали город: {city.city} ({info_the_city['country']})\n"
            f"Температура составляет {info_the_city['temperature']} °C\n"
            f"Влажность составляет {info_the_city['humidity']} %\n"
            f"Погода, если описать двумя словами: "
            f"{info_the_city['description']}\n"
            f"Ветер до {info_the_city['wind_speed']} м/с, порывами "
            f"до {info_the_city['wind_gust'] if info_the_city['wind_gust'] else info_the_city['wind_speed']} м/с\n"
            f"Солнышко встанет в {info_the_city['sunrise']} "
            f"и зайдет в {info_the_city['sunset']}")
    return text
