import { useEffect, useState } from 'react'
import siteMetadata from '@/data/siteMetadata'
import headerNavLinks from '@/data/headerNavLinks'
import Logo from '@/data/logo.svg'
import Link from './Link'
import SectionContainer from './SectionContainer'
import Footer from './Footer'
import MobileNav from './MobileNav'
import MobileNavTrigger from './MobileNavTrigger'
import ThemeSwitch from './ThemeSwitch'

const LayoutWrapper = ({ children }) => {
  const [navShow, setNavShow] = useState(false)
  const [scrollY, setScrollY] = useState(0)

  useEffect(() => {
    const handleScroll = () => {
      setScrollY(window.scrollY)
    }

    // just trigger this so that the initial state
    // is updated as soon as the component is mounted
    // related: https://stackoverflow.com/a/63408216
    handleScroll()

    window.addEventListener('scroll', handleScroll)
    return () => {
      window.removeEventListener('scroll', handleScroll)
    }

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const onToggleNav = () => {
    setNavShow((status) => {
      if (status) {
        document.body.style.overflow = 'auto'
      } else {
        // Prevent scrolling
        document.body.style.overflow = 'hidden'
      }

      return !status
    })
  }

  return (
    <>
      <MobileNav navShow={navShow} onToggleNav={onToggleNav} />
      <header
        className={`supports-backdrop-blur:bg-white/95 fixed top-0 z-30 w-full overflow-hidden bg-white/75 py-3 backdrop-blur transition-colors delay-150 duration-500 ease-in-out ${
          scrollY > 0 ? 'dark:bg-octonary/75' : 'bg-transparent'
        }`}
      >
        <div className="mx-auto flex max-w-3xl items-center justify-between px-3 xl:max-w-5xl xl:px-0">
          <div>
            <Link href="/" aria-label={siteMetadata.headerTitle}>
              <div className="flex items-center justify-between">
                <div className="mr-3">
                  <Logo />
                </div>
                {typeof siteMetadata.headerTitle === 'string' ? (
                  <div className="-mt-2 hidden h-6 font-quicksand text-2xl font-normal hover:text-primary-500 sm:block">
                    {siteMetadata.headerTitle}
                  </div>
                ) : (
                  siteMetadata.headerTitle
                )}
              </div>
            </Link>
          </div>
          <div className="flex items-center text-base leading-5">
            <div className="hidden sm:block">
              {headerNavLinks.map((link) => (
                <Link
                  key={link.title}
                  href={link.href}
                  className=" relative font-quicksand font-bold hover:text-primary-600 dark:text-gray-100 dark:hover:text-primary-400 sm:p-4"
                >
                  {link.title}
                </Link>
              ))}
            </div>
            <ThemeSwitch />
            <MobileNavTrigger navShow={navShow} onToggleNav={onToggleNav} />
          </div>
        </div>
      </header>
      <SectionContainer>
        <div className="flex h-screen flex-col justify-between pt-40">
          <main className="mb-auto">{children}</main>
          <Footer />
        </div>
      </SectionContainer>
    </>
  )
}

export default LayoutWrapper
