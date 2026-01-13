import pickle
import numpy as np
import time
import random

model = pickle.load(open("model.pkl", "rb"))
proto_encoder = pickle.load(open("proto.pkl", "rb"))
flag_encoder = pickle.load(open("flag.pkl", "rb"))

logs = []
normal_count = 0
attack_count = 0

def simulate_packet():
    duration = random.randint(0, 2)
    protocol_type = random.choice(["tcp", "udp"])
    src_bytes = random.randint(0, 500)
    dst_bytes = random.randint(0, 800)
    flag = random.choice(["SF", "REJ"])
    return [duration, protocol_type, src_bytes, dst_bytes, flag]

def detect():
    global normal_count, attack_count

    while True:
        features = simulate_packet()

        protocol = proto_encoder.transform([features[1]])[0]
        flag = flag_encoder.transform([features[4]])[0]

        data = np.array([[features[0], protocol, features[2], features[3], flag]])
        prediction = model.predict(data)[0]

        if prediction == 1:
            msg = "🚨 Attack Detected"
            attack_count += 1
        else:
            msg = "✅ Normal Traffic"
            normal_count += 1

        logs.append(msg)
        if len(logs) > 20:
            logs.pop(0)

        print(msg)
        time.sleep(2)
