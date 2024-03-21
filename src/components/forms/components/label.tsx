export default function FormLabel(props: { children: React.ReactNode, htmlFor: string }) {
  return (
      <label className="block mb-2 font-medium text-gray-700" {...props}>
        {props.children}
      </label>
  )
}
