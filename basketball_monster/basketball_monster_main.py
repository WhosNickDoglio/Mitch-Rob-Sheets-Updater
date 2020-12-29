from basketball_monster.scraper import BasketballMonsterWebScraper
import player_data_converter


def main():
    scraper = BasketballMonsterWebScraper()
    data = scraper.parse_data()

    player_info = map(player_data_converter.convert_element_to_player_info, data)

    for player in player_info:
        print(player)


if __name__ == "__main__":
    main()
