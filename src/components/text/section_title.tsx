export default function SectionTitle(props: { children: React.ReactNode }) {
  return (
      <h2 className="text-3xl font-bold mb-4">
        {props.children}
      </h2>
  )
}
