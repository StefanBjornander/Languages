import Link from './Link'
import headerNavLinks from '@/data/headerNavLinks'

const MobileNav = (props) => {
  return (
    <div className="sm:hidden">
      <div
        className={`supports-backdrop-blur:bg-white/95 fixed top-0 right-0 z-40 h-full w-full transform bg-gray-200 opacity-95 backdrop-blur duration-300 ease-in-out dark:bg-octonary/75 ${
          props.navShow ? 'translate-x-0' : 'translate-x-full'
        }`}
      >
        <button
          type="button"
          aria-label="toggle modal"
          className="fixed h-full w-full cursor-auto focus:outline-none"
          onClick={props.onToggleNav}
        ></button>
        <nav className="fixed mt-8 h-full">
          {headerNavLinks.map((link) => (
            <div key={link.title} className="px-12 py-4">
              <Link
                href={link.href}
                className="text-2xl font-bold tracking-widest text-gray-900 dark:text-gray-100"
                onClick={props.onToggleNav}
              >
                {link.title}
              </Link>
            </div>
          ))}
        </nav>
      </div>
    </div>
  )
}

export default MobileNav
