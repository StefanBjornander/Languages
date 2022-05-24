export default function PageTitle({ children }) {
  return (
    <h1 className="relative font-quicksand text-4xl leading-9 tracking-tight text-primary-500 sm:text-4xl sm:leading-10 md:text-6xl md:leading-14">
      {children}
    </h1>
  )
}
