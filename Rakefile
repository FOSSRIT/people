abort('Please run this using `bundle exec rake`') unless ENV["BUNDLE_BIN_PATH"]
require 'html-proofer'

desc "Build website with jekyll and test with html-proofer"
task :test do
  sh "bundle exec jekyll build"
  options = {
    :check_html => true,
    :empty_alt_ignore => true,
    :http_status_ignore => [0,999],
    :cache => {
      :timeframe => '6w'
    }
  }
  HTMLProofer.check_directory("./_site/", options).run
end

task :default => [:test]
