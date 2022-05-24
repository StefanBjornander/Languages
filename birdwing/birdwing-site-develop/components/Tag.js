import Link from 'next/link'
import kebabCase from '@/lib/utils/kebabCase'

const Tag = ({ text }) => {
  return (
    <Link href={`/tags/${kebabCase(text)}`}>
      <a className="mr-3 rounded-full bg-primary-500 px-2 text-xs font-bold uppercase text-octonary hover:bg-primary-600 dark:hover:bg-primary-400">
        {text.split(' ').join('-')}
      </a>
    </Link>
  )
}

export default Tag
