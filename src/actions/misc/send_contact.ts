'use server'

import { Resend } from 'resend';
const resend = new Resend(process.env.RESEND_API_KEY);

export async function sendContact(prevState: any, formData: FormData) {
  // Send a contact email via sendgrid

  try {
    await resend.emails.send({
      from: "onboarding@resend.dev",
      to: process.env.NODE_ENV === "development" ? "delivered@resend.dev" : 'awwester@gmail.com',
      subject: `Message from ${formData.get("name")}`,
      text: formData.get("message") as string,
      reply_to: formData.get("email") as string,
    });
    // Send a success response
    return {message: "Email sent successfully!", success: true}
  } catch (error) {
    // Send an error response
    return {message: "Sorry, something went wrong, please try again later.", success: false}
  }
}
