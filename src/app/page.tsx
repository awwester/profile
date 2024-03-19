import Image from "next/image";


export default function Home() {
  const projects = [
        { title: 'Lead Sherpa', description: 'Real Estate Investment Platform', image: '/images/projects/leadsherpa.png' },
        { title: 'Project City', description: 'Learning platform for animated movies and art', image: '/images/projects/project_city.png' },
        { title: 'Joe Coffee', description: 'Mobile ordering for independent coffee shops', image: '/images/projects/joe_coffee.png' },
        { title: 'Bnb Sync', description: 'AirBnb integration with Xero accounting', image: '/images/projects/bnbsync.png' },
        { title: 'Frontier Signal', description: 'Usage of data science to improve hiring', image: '/images/projects/frontier_signal.png' },
        { title: 'Real Life Global', description: 'Online English learning platform', image: '/images/projects/real_life_global.png' },
        { title: 'Vested Yeti', description: 'Social web browsing', image: '/images/projects/vested_yeti.png' },
        { title: 'Go Advocate', description: 'Canadian Political Campaigns', image: '/images/projects/goadvocate.png' },
    ];

    return (
        <div className="bg-gray-100 min-h-screen">
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
            <section id="about" className="container mx-auto py-32">
                <h2 className="text-3xl font-bold mb-4">About Me</h2>
                <p className="text-gray-700">I am Adam Wester, a software developer with over 15 years of experience in the industry. I specialize in working with small to medium-sized startups, focusing on building SaaS companies from ideation to execution. With a passion for innovation and problem-solving, I strive to create scalable and efficient solutions that drive business growth.</p>
            </section>

            {/* Projects Section */}
            <section id="projects" className="bg-slate-200 py-16 border-slate-300 border-y-2">
                <div className="container mx-auto">
                    <h2 className="text-3xl font-bold mb-4">Projects</h2>
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
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </section>

            {/* Contact Section */}
            <section id="contact" className="container mx-auto py-32">
                <h2 className="text-3xl font-bold mb-4">Contact Me</h2>
                <p className="text-gray-700">Feel free to reach out to me for any inquiries or collaboration opportunities:</p>
                <ul className="mt-4">
                    <li className="flex items-center">
                        <svg className="h-5 w-5 text-blue-500 mr-2" fill="none" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" viewBox="0 0 24 24">
                            <path d="M22 2L2 22h20zm0 0L2 2v20z"></path>
                        </svg>
                        <span>LinkedIn: linkedin.com/in/awwester</span>
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
