import csv
import requests


def download_youbike_data() -> list[dict]:
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.get(youbike_url)
    response.raise_for_status()
    print("下載成功")
    return response.json()


def save_to_csv(data: list[dict], csv_filename: str):
    # 檢查數據是否為空
    if not data:
        print("數據為空，無法生成CSV文件。")
        return

    # 提取列名（CSV的標題行）
    header = data[0].keys()

    # 寫入CSV文件
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=header)

        # 寫入標題行
        csv_writer.writeheader()

        # 寫入數據行
        csv_writer.writerows(data)


if __name__ == "__main__":
    youbike_data = download_youbike_data()
    save_to_csv(youbike_data, 'youbike_data.csv')
    print("轉換成功，已保存為 ybike_data.csv")
