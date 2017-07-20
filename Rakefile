REMOTE_ADDRESS="pi@raspberrypi.local"

namespace :raspi do
	desc "send bin/"
	task :send do
		puts `rsync -avz bin/ #{REMOTE_ADDRESS}:bin/`
	end

	desc "get picture"
	task :get_pic do
		puts `rsync -avz #{REMOTE_ADDRESS}:Picture/ picture/`
	end
end
