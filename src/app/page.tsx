import Image from "next/image";

import SectionTitle from "@/components/text/section_title";
import ProjectTag from "@/components/project_tag";


export default function Home() {
  const projects = [
        { title: 'Lead Sherpa', description: 'Real Estate Investment Platform', image: '/images/projects/leadsherpa.png', tags: ['Django Rest Framework', 'React', 'Twilio', 'AWS', 'Braintree', 'PWA', 'Telnyx'] },
        { title: 'Project City', description: 'Learning platform for animated movies and art', image: '/images/projects/project_city.png', tags: ['Django Rest Framework', 'React', 'Stripe', 'React Native', 'AWS'] },
        { title: 'Go Advocate', description: 'Canadian political campaigns with calls, email, and letters', image: '/images/projects/goadvocate.png', tags: ['Django', 'AWS', 'Stripe', 'Twilio', 'OpenAI'] },
        { title: 'Joe Coffee', description: 'Mobile ordering for independent coffee shops', image: '/images/projects/joe_coffee.png', tags: ['Django Rest Framework', 'Heroku', 'Stripe', 'React'] },
        { title: 'Bnb Sync', description: 'AirBnb integration with Xero accounting', image: '/images/projects/bnbsync.png', tags: ['Django Rest Framework', 'React', 'AWS', 'Stripe', 'Xero', 'AirBnb'] },
        { title: 'Frontier Signal', description: 'Usage of data science to improve hiring', image: '/images/projects/frontier_signal.png', tags: ['Django', 'Heroku'] },
        { title: 'Real Life Global', description: 'Online English learning platform', image: '/images/projects/real_life_global.png', tags: ['Django Rest Framework', 'Ember.js', 'AWS'] },
        { title: 'Vested Yeti', description: 'Social web browsing', image: '/images/projects/vested_yeti.png', tags: ['Django Rest Framework', 'React', 'Chrome Extension', 'React Native', 'AWS'] },
    ];

    return (
        <div className="bg-white min-h-screen">
            <nav className="bg-blue-500 py-4">
                <div className="container mx-auto flex justify-between items-center">
                    <div className="text-white font-bold text-xl">Adam Wester - SaaS Specialist</div>
                    <ul className="flex space-x-4">
                        <li><a href="#about" className="text-white">About</a></li>
                        <li><a href="#projects" className="text-white">Projects</a></li>
                        <li><a href="#contact" className="text-white">Contact</a></li>
                    </ul>
                </div>
            </nav>

            {/* About Section */}
            <section id="about" className="container mx-auto py-32 flex items-center">
                <div className="mr-16">
                  <Image src="/images/logos/adam.jpg" alt="Adam Wester" width={600} height={600} className="rounded-full" />
                </div>
                <div>
                  <SectionTitle>About Me</SectionTitle>
                  <p className="text-gray-700">I am Adam Wester, a software developer and engineering manager with over 15 years of experience in the industry. I specialize in building SaaS solutions for small to medium-sized startups, focusing on building from ideation to execution. With a passion for business and problem-solving, I strive to create scalable and efficient solutions that drive business growth.</p>
                </div>
            </section>

            {/* Projects Section */}
            <section id="projects" className="bg-slate-200 py-16 border-slate-300 border-y-2">
                <div className="container mx-auto">
                    <SectionTitle>Projects</SectionTitle>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-32">
                        {projects.map((project, index) => (
                            <div key={index} className="bg-white shadow-md rounded">
                                <div className="relative">
                                  <Image
                                    src={project.image}
                                    alt={project.title}
                                    style={{ position: "relative", width: "100%", height: "auto" }} width={1000} height={500}
                                    className="rounded-t"
                                  />
                                </div>
                                <div className="p-4">
                                  <h3 className="text-xl font-bold mb-2">{project.title}</h3>
                                  <p className="text-gray-700">{project.description}</p>
                                  <div className="mt-4">
                                      {project.tags.map((tag, index) => <ProjectTag key={index}>{tag}</ProjectTag>)}
                                  </div>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </section>

            {/* Contact Section */}
            <section id="contact" className="container mx-auto py-32">
                <SectionTitle>Contact me</SectionTitle>
                <p className="text-gray-700">Feel free to reach out to me for any inquiries or collaboration opportunities:</p>
                <ul className="mt-4">
                    <li className="flex items-center">
                        <svg className="h-5 w-5 text-blue-500 mr-2" fill="none" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" viewBox="0 0 24 24">
                            <path d="M22 2L2 22h20zm0 0L2 2v20z"></path>
                        </svg>
                        <span><a href="https://www.linkedin.com/in/awwester" target="_blank">LinkedIn</a></span>
                    </li>
                </ul>
            </section>

            {/* Footer */}
            <footer className="bg-blue-500 text-white py-4">
                <div className="container mx-auto text-center">
                    <p>&copy; {new Date().getFullYear()} Adam Wester. All rights reserved.</p>
                </div>
            </footer>
        </div>
    );
}
