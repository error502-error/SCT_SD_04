import requests
from bs4 import BeautifulSoup
import csv

def scrape_products(url):
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise error if request failed

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find product containers - this selector depends on the website structure
    # For this generic example, assume products are in divs with class 'product'
    products = soup.find_all('div', class_='product')

    product_list = []

    for product in products:
        # Extract product name
        name_tag = product.find('h2', class_='product-name')
        name = name_tag.text.strip() if name_tag else 'N/A'

        # Extract price
        price_tag = product.find('span', class_='price')
        price = price_tag.text.strip() if price_tag else 'N/A'

        # Extract rating
        rating_tag = product.find('div', class_='rating')
        rating = rating_tag.text.strip() if rating_tag else 'N/A'

        product_list.append({
            'Name': name,
            'Price': price,
            'Rating': rating
        })

    return product_list

def save_to_csv(products, filename):
    # Define CSV column names
    fieldnames = ['Name', 'Price', 'Rating']

    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for product in products:
            writer.writerow(product)

if __name__ == '__main__':
    # Example URL - replace with actual e-commerce page URL
    url = 'https://example.com/products'

    try:
        products = scrape_products(url)
        if products:
            save_to_csv(products, 'products.csv')
            print(f'Successfully saved {len(products)} products to products.csv')
        else:
            print('No products found on the page.')
    except Exception as e:
        print(f'Error occurred: {e}')
