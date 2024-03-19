export default function ProjectTag(props: { children: React.ReactNode }) {
  // Show a tag of a technology used on a project.
  return (
    <span className="bg-blue-500 text-white text-xs font-bold rounded-full px-2 py-1 mx-2">
      {props.children}
    </span>
  )
}
