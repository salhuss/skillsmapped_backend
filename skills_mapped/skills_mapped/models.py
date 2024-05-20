from django.db import models

class AccreditedSchool(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Work Experiences"

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class Reference(models.Model):
    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    # Additional Personal Information
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    ethnicity = models.CharField(max_length=100, null=True, blank=True)

    # Education
    education_level = models.CharField(max_length=100)
    school_name = models.ForeignKey(AccreditedSchool, on_delete=models.SET_NULL, null=True, blank=True)
    degree = models.CharField(max_length=100)
    graduation_year = models.PositiveIntegerField()

    # Work Experience
    work_experiences = models.ManyToManyField(WorkExperience, blank=True)

    # Skills
    skills = models.TextField()

    # Job Preferences
    job_type = models.CharField(max_length=20, choices=[
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
        ('Remote', 'Remote'),
        ('Other', 'Other'),
    ], default='Full-time')
    area_preference = models.CharField(max_length=100)
    industry_preference = models.CharField(max_length=100)

    # Salary Expectation
    salary_expectation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Availability
    available_start_date = models.DateField()
    available_end_date = models.DateField(blank=True, null=True)
    specific_availability_details = models.TextField(null=True, blank=True)

    # Languages
    languages = models.TextField(null=True, blank=True)

    # Certifications
    certifications = models.TextField(null=True, blank=True)

    # Portfolio
    portfolio_link = models.URLField(null=True, blank=True)

    # References
    references = models.ManyToManyField(Reference, blank=True)

    # Address
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    # Interview Notes
    interview_notes = models.TextField(null=True, blank=True)

    # Document Tracking
    resume_received = models.BooleanField(default=False)
    references_checked = models.BooleanField(default=False)
    background_check_completed = models.BooleanField(default=False)

    # Data Privacy Compliance
    data_processing_consent = models.BooleanField(default=False)

    # Preferred Contact Method
    CONTACT_METHOD_CHOICES = [
        ('Email', 'Email'),
        ('Phone', 'Phone'),
        ('Text', 'Text'),
    ]
    preferred_contact_method = models.CharField(max_length=10, choices=CONTACT_METHOD_CHOICES, default='Email')

    # Soft Skills
    soft_skills = models.TextField(null=True, blank=True)

    # Remote Work Experience
    remote_work_experience = models.TextField(null=True, blank=True)

    # Social Media Profiles
    linkedin_profile = models.URLField(null=True, blank=True)
    github_profile = models.URLField(null=True, blank=True)

    # Volunteer Experience
    volunteer_experience = models.TextField(null=True, blank=True)

    # Professional Development
    professional_development = models.TextField(null=True, blank=True)

    # Work Authorization
    work_authorization_status = models.CharField(max_length=100, null=True, blank=True)
    visa_type = models.CharField(max_length=100, null=True, blank=True)
    visa_expiration_date = models.DateField(null=True, blank=True)

    # Relocation Preferences
    relocation_willingness = models.BooleanField(default=False)
    relocation_preferences = models.TextField(null=True, blank=True)

    # Feedback
    recruiter_feedback = models.TextField(null=True, blank=True)

    # Offer Details
    offer_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    offer_benefits = models.TextField(null=True, blank=True)
    offer_start_date = models.DateField(null=True, blank=True)

    # Onboarding Information
    onboarding_information = models.TextField(null=True, blank=True)

    # Retention Information
    reasons_for_leaving = models.TextField(null=True, blank=True)
    job_satisfaction_factors = models.TextField(null=True, blank=True)

    # Performance Reviews
    performance_review_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    performance_review_comments = models.TextField(null=True, blank=True)
    performance_review_goals = models.TextField(null=True, blank=True)

    # Exit Interviews
    exit_interview_feedback = models.TextField(null=True, blank=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
