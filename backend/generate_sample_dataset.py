"""
Sample Dataset Generator
Creates a sample fake_jobs.csv for testing when Kaggle dataset is not available
"""
import pandas as pd
import random

def generate_fake_jobs(n=50):
    """Generate fake job postings"""
    fake_titles = [
        "Work From Home - Easy Money",
        "Get Rich Quick - No Experience",
        "Earn $10,000 Per Week",
        "Make Money Online Fast",
        "Home Based Business Opportunity",
        "Urgent Hiring - High Pay",
        "No Experience Required - Big Salary",
        "Easy Work From Home Job",
        "Quick Cash Opportunity",
        "Immediate Start - No Interview"
    ]
    
    fake_companies = [
        "Unknown Company",
        "Quick Money Inc",
        "Easy Cash Corp",
        "Home Business Ltd",
        "Fast Money Group",
        "Suspicious Company",
        "No Name Business",
        "Untraceable Corp"
    ]
    
    fake_descriptions = [
        "Make thousands of dollars from home with no effort! Just send us $99 for training materials and start earning immediately!",
        "Urgent hiring! Work from home and earn big money fast. No experience needed. Contact us now!",
        "Amazing opportunity to earn $5000 per week from home. No skills required. Just pay a small registration fee.",
        "Get rich quick with our proven system. Send money for starter kit and begin your journey to wealth!",
        "Work from home doing simple tasks. Earn $100 per hour. Pay $50 registration fee to get started.",
        "Immediate hiring! No interview needed. Just send your personal information and bank details.",
        "Make money online easily. No experience required. Send payment for training and start today!",
        "Guaranteed income from home. Pay small fee for materials and earn thousands weekly!",
        "Easy money opportunity. Work whenever you want. Just provide credit card for verification.",
        "Urgent positions available. High pay, no experience. Send money for background check."
    ]
    
    fake_requirements = [
        "No experience needed",
        "Anyone can apply",
        "Just need internet connection",
        "No qualifications required",
        "Must pay registration fee",
        "Send personal information",
        "Provide bank details",
        "Pay for training materials"
    ]
    
    jobs = []
    for _ in range(n):
        job = {
            'title': random.choice(fake_titles),
            'company_profile': random.choice(fake_companies),
            'description': random.choice(fake_descriptions),
            'requirements': random.choice(fake_requirements),
            'fraudulent': 1
        }
        jobs.append(job)
    
    return jobs

def generate_genuine_jobs(n=50):
    """Generate genuine job postings"""
    genuine_titles = [
        "Software Engineer",
        "Data Scientist",
        "Product Manager",
        "Marketing Manager",
        "Business Analyst",
        "UX Designer",
        "DevOps Engineer",
        "Full Stack Developer",
        "Project Manager",
        "Sales Executive"
    ]
    
    genuine_companies = [
        "ABC Technology Inc",
        "XYZ Software Solutions",
        "Global Tech Corp",
        "Innovation Labs",
        "Digital Solutions Ltd",
        "Tech Innovations Inc",
        "Software Systems Corp",
        "Data Analytics Group"
    ]
    
    genuine_descriptions = [
        "We are seeking a talented professional to join our growing team. The ideal candidate will work on challenging projects and collaborate with experienced team members.",
        "Join our dynamic team and contribute to innovative projects. We offer competitive compensation and excellent benefits package.",
        "Established company looking for skilled professional. You will be responsible for developing solutions and working with cross-functional teams.",
        "Exciting opportunity to work with cutting-edge technology. We value innovation and provide opportunities for professional growth.",
        "We are hiring for a key position in our organization. The role involves strategic planning and execution of important initiatives.",
        "Looking for experienced professional to lead projects and mentor junior team members. Competitive salary and benefits offered.",
        "Join a fast-growing company with excellent career prospects. Work on meaningful projects with talented colleagues.",
        "Seeking qualified candidate for important role. Responsibilities include project management and stakeholder communication."
    ]
    
    genuine_requirements = [
        "Bachelor's degree in Computer Science or related field, 3+ years experience",
        "Master's degree preferred, 5 years of relevant experience, strong technical skills",
        "BS/BA degree, 2-4 years experience, excellent communication skills",
        "Relevant degree, proven track record, proficiency in required technologies",
        "University degree, 3+ years in similar role, team player with leadership skills",
        "Bachelor's degree, experience with modern frameworks, problem-solving abilities",
        "Degree in relevant field, industry experience, strong analytical skills",
        "Educational qualification, professional experience, technical expertise required"
    ]
    
    jobs = []
    for _ in range(n):
        job = {
            'title': random.choice(genuine_titles),
            'company_profile': random.choice(genuine_companies) + " is a well-established company with years of industry experience.",
            'description': random.choice(genuine_descriptions),
            'requirements': random.choice(genuine_requirements),
            'fraudulent': 0
        }
        jobs.append(job)
    
    return jobs

def create_sample_dataset(fake_count=100, genuine_count=100, output_file='fake_jobs.csv'):
    """Create and save sample dataset"""
    print(f"Generating sample dataset...")
    print(f"Fake jobs: {fake_count}")
    print(f"Genuine jobs: {genuine_count}")
    
    # Generate jobs
    fake_jobs = generate_fake_jobs(fake_count)
    genuine_jobs = generate_genuine_jobs(genuine_count)
    
    # Combine and shuffle
    all_jobs = fake_jobs + genuine_jobs
    random.shuffle(all_jobs)
    
    # Create DataFrame
    df = pd.DataFrame(all_jobs)
    
    # Save to CSV
    df.to_csv(output_file, index=False)
    
    print(f"\nDataset created successfully!")
    print(f"Total records: {len(df)}")
    print(f"Saved to: {output_file}")
    print(f"\nDistribution:")
    print(f"Fake: {df['fraudulent'].sum()}")
    print(f"Genuine: {len(df) - df['fraudulent'].sum()}")
    
    return df

if __name__ == "__main__":
    # Create sample dataset with 200 jobs (100 fake, 100 genuine)
    df = create_sample_dataset(fake_count=100, genuine_count=100)
    
    # Display sample
    print("\n" + "="*60)
    print("Sample Records:")
    print("="*60)
    print("\nFake Job Example:")
    print(df[df['fraudulent'] == 1].iloc[0].to_dict())
    print("\nGenuine Job Example:")
    print(df[df['fraudulent'] == 0].iloc[0].to_dict())
