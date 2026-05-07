import requests

def read_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return None
    finally:
        print("Execution complete.")

# Test
print(read_url('https://jsonplaceholder.typicode.com/posts/1'))
print(read_url('https://nonexistent.url'))