from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample job data (replace with your actual scraped data)
job_data = []

@app.route('/jobs', methods=['GET'])
def get_all_jobs():
    return jsonify(job_data)

@app.route('/jobs/search', methods=['GET'])
def search_jobs():
    location = request.args.get('location')
    job_title = request.args.get('job_title')

    # Implement search logic based on location and job title
    # Replace this with your actual search code

    # Sample search results (replace with your actual search results)
    search_results = [job for job in job_data if
                      location.lower() in job['location'].lower() and
                      job_title.lower() in job['title'].lower()]

    return jsonify(search_results)

if __name__ == '__main__':
    app.run(debug=True)
