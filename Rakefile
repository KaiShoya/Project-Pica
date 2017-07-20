USER="pi"
IP="raspberrypi.local"
REMOTE_ADDRESS="#{USER}@#{IP}"
PROJECT="Project-Pica"

namespace :raspi do
	desc "Initial setup #{PROJECT}."
	task :init do
		puts `ssh #{REMOTE_ADDRESS} "sudo mkdir /opt/#{PROJECT} && sudo chown #{USER}:#{USER} /opt/#{PROJECT} && ln -s /opt/#{PROJECT}"`
		puts `rsync -avz --exclude=".git*" --exclude="Picture/" ./ #{REMOTE_ADDRESS}:#{PROJECT}/`
	end

	desc "Sync Project-Pica && set bin/"
	task :sync do
		puts `rsync -avz --delete --exclude=".git*" --exclude="Picture/" ./ #{REMOTE_ADDRESS}:#{PROJECT}/`
		`ssh #{REMOTE_ADDRESS} "ln -s /opt/#{PROJECT}/{bin/*,sample/*} bin/ && find bin/ -xtype l -exec rm -f {} \;" &> /dev/null`
	end

	desc "get picture"
	task :get_pic do
		puts `rsync -avz #{REMOTE_ADDRESS}:Picture/ picture/`
	end
end
