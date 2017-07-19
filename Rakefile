IP="pi@raspberrypi.local"

namespace :raspi do
	desc "send bin/"
	task :send do
		puts `rsync -avz bin/ #{IP}:bin/`
	end

	desc "get picture"
	task :get_pic do
		puts `rsync -avz #{IP}:Picture/ picture/`
	end
end
