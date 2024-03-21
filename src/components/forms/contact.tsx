"use client"

import { useFormState, useFormStatus } from 'react-dom'

import { sendContact } from '@/actions/misc/send_contact'
import FormInput from './components/input'
import FormTextarea from './components/textarea'
import FormLabel from './components/label'
import { useEffect, useRef } from 'react'


export default function ContactForm() {

    const [state, formAction] = useFormState(sendContact, null)
    const { pending } = useFormStatus()
    const ref = useRef<HTMLFormElement>(null)

    useEffect(() => {
      if (state?.success) {
        ref?.current?.reset()
      }
    }, [state?.success])

    return (
      <form action={formAction} ref={ref} className="max-w-md mt-8">
        <div className="mb-4">
          <FormLabel htmlFor="name">
            Name
          </FormLabel>
          <FormInput
            type="text"
            id="name"
            name="name"
            required
          />
        </div>
        <div className="mb-4">
          <FormLabel htmlFor="email">
            Email
          </FormLabel>
          <FormInput
            type="email"
            id="email"
            name="email"
            required
          />
        </div>
        <div className="mb-4">
          <FormLabel htmlFor="message">
            Explain the collaboration you seek
          </FormLabel>
          <FormTextarea
            id="message"
            name="message"
            className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            rows={6}
            required
          ></FormTextarea>
        </div>
        <button
          type="submit"
          className="w-full px-4 py-2 text-white bg-blue-500 rounded-md hover:bg-blue-600 focus:outline-none focus:bg-blue-600"
          disabled={pending}
        >
          Send
        </button>
        {state?.message && (
          <p className={`mt-4 font-bold text-${state?.success ? 'green' : 'red'}-500`}>
            {state?.message}
          </p>
        )}
      </form>
    )
}
