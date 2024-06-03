import os
import time
import io
import requests
import multiprocessing

from pypdf import PdfReader
from multiprocessing import Pool
import urllib.request
from urllib.parse import urlparse
import fitz

def read_page_fitz(vector):
   
    # recreate the arguments
    idx = vector[0]  # this is the segment number we have to process
    cpu = vector[1]  # number of CPUs
    filename = vector[2]  # document filename
    # doc = fitz.open(filename)  # open the document
    doc=fitz.open(stream=filename, filetype="pdf")
    num_pages = doc.page_count  # get number of pages
    seg_size = int(num_pages / cpu + 1)
    seg_from = idx * seg_size  # our first page number
    seg_to = min(seg_from + seg_size, num_pages)  # last page number
    res = []
    print("Pages range:",seg_from, seg_to)
    for i in range(seg_from, seg_to):  # work through our page segment
        page = doc[i]
        # page.get_text("rawdict")  # use any page-related type of work here, eg
        res.append(page.get_text())
    return " ".join(res)

def read_pdf_parallel_fitz(url):
    cpu = os.cpu_count()
    print("CPU Count:",cpu)
    start_time = time.time()
    # a = urlparse(url)         
    # file_name = os.path.basename(a.path)
    # urllib.request.urlretrieve(url, file_name)
    response = requests.get(url)
    file = io.BytesIO(response.content)
    print("File download time:",time.time()-start_time)
    # filename = "file_in.pdf"
    # filename = file_name

    # make vectors of arguments for the processes
    vectors = [(i, cpu, file) for i in range(cpu)]
    # vectors = [(i, cpu, filename) for i in range(cpu)]
    # print("Starting %i processes for '%s'." % (cpu, filename))

    with Pool(processes=os.cpu_count()) as pool:
        # results = pool.map(read_single_page_up, page_list)
        results = pool.map(read_page_fitz, vectors)

    text = " ".join(results)
    return text

def process_multiple_url(url_list):
    with Pool(processes=os.cpu_count()) as pool:
        # results = pool.map(read_single_page_up, page_list)
        results = pool.map(read_pdf_parallel_fitz, url_list)
    text = " ".join(results)
    return text

if __name__ == '__main__':
    # url = "https://www.tesla.com/ns_videos/2022-tesla-impact-report.pdf"
    # start_time = time.time()
    # res = read_pdf_parallel_fitz(url)
    # print("Total time usign Pymudf(s):",time.time()-start_time)
    url1 = "https://ir.tesla.com/_flysystem/s3/sec/000095017021002253/tsla-20210930-gen.pdf"
    url2 = "https://ir.tesla.com/_flysystem/s3/sec/000095017023001409/tsla-20221231-gen.pdf"
    url_list = [url1, url2]
    start_time = time.time()
    res = process_multiple_url(url_list)
    print(f"For {len(url_list)} docs total time usign Pymudf(s):{time.time()-start_time}")
  