"""
API Testing Script
Test all endpoints of the Fake Job Detection API
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health check endpoint"""
    print("\n=== Testing Health Check ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_root():
    """Test root endpoint"""
    print("\n=== Testing Root Endpoint ===")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_predict_text_fake():
    """Test text prediction with fake job"""
    print("\n=== Testing Text Prediction (Fake Job) ===")
    
    fake_job = """
    URGENT HIRING! Work from home and earn $5000 per week!
    No experience needed! No interview required!
    Just send $99 for training materials and start earning immediately!
    Contact us now! Limited slots available!
    """
    
    response = requests.post(
        f"{BASE_URL}/predict-text",
        json={"text": fake_job}
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_predict_text_genuine():
    """Test text prediction with genuine job"""
    print("\n=== Testing Text Prediction (Genuine Job) ===")
    
    genuine_job = """
    Software Engineer - ABC Technology Inc.
    
    About the Company:
    ABC Technology is a leading software development company with 15 years of experience.
    
    Job Description:
    We are seeking a talented Software Engineer to join our development team.
    
    Requirements:
    - Bachelor's degree in Computer Science or related field
    - 3+ years of experience in Python development
    - Strong knowledge of Django and Flask frameworks
    - Experience with RESTful APIs and databases
    - Good communication and teamwork skills
    
    Responsibilities:
    - Develop and maintain web applications
    - Write clean, maintainable code
    - Collaborate with cross-functional teams
    - Participate in code reviews
    
    Compensation:
    - Salary: $80,000 - $100,000 per year
    - Health insurance
    - 401(k) matching
    - Paid time off
    
    How to Apply:
    Send your resume to careers@abctech.com
    """
    
    response = requests.post(
        f"{BASE_URL}/predict-text",
        json={"text": genuine_job}
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_model_info():
    """Test model info endpoint"""
    print("\n=== Testing Model Info ===")
    response = requests.get(f"{BASE_URL}/model-info")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_predictions():
    """Test get predictions endpoint"""
    print("\n=== Testing Get Predictions ===")
    response = requests.get(f"{BASE_URL}/predictions?limit=5")
    print(f"Status Code: {response.status_code}")
    result = response.json()
    print(f"Count: {result.get('count', 0)}")
    if result.get('predictions'):
        print(f"Latest Prediction: {json.dumps(result['predictions'][0], indent=2)}")

def run_all_tests():
    """Run all API tests"""
    print("=" * 60)
    print("FAKE JOB DETECTION API - TEST SUITE")
    print("=" * 60)
    
    try:
        test_health()
        test_root()
        test_model_info()
        test_predict_text_fake()
        test_predict_text_genuine()
        test_predictions()
        
        print("\n" + "=" * 60)
        print("ALL TESTS COMPLETED")
        print("=" * 60)
        
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Cannot connect to API server")
        print("Make sure the backend server is running:")
        print("  cd backend")
        print("  uvicorn app.main:app --reload")
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")

if __name__ == "__main__":
    run_all_tests()
