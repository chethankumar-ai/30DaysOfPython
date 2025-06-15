# -  Download multiple files concurrently using threads
import threading
import requests
def download_file(url):
    response = requests.get(url)
    filename = url.split("/")[-1]
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"Downloaded {filename}") 
def download_files_concurrently(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_file, args=(url,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
# Example usage
if __name__ == "__main__":
    urls = [
        "https://example.com/file1.txt",
        "https://example.com/file2.txt",
        "https://example.com/file3.txt",
        "https://example.com/file4.txt"
    ]
    download_files_concurrently(urls)
    print("All files downloaded.")