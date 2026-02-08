for c in range(23):
  y=['renuraj',  'rabilakshan', 'kirshigan', 'monikka', 'nikithan', 'lucshman', 'sayanudan', 'perushan', 'ragul', 'thuwaarahaa', 'mayurresh', 'lathushan', 'shabareesan', 'kirshikeshan', 'abikeerthan', 'thakshanna', 'danushtan', 'deluxinie', 'yogavi' ,'rakshana', 'rakshika', 'kutralan']
  x=y[c]
  print("Name:-",x)
  a = ['சரவணபவன் தாமிரன் அண்ணா ','சிவகுமார் அருண் அண்ணா ','மேகவண்ணன் வருண் அண்ணா ','விஜயானந்தமூர்த்தி அபிஷேக் அண்ணா ','ஸ்ரீ சுஜானி சிவயோகேஸ்வரஷர்மா அக்கா ','ராஜாராம் சூர்யா அண்ணா ','ஜெகதீஸ்வரன் கிரியங்கரன் அண்ணா ','சந்திரகுமார் தர்ஷன் அண்ணா ','ஹரிஷனா சுரேஷ்குமார் அக்கா ','ஷஹானா சின்னையா அக்கா  ','பவிஷா தவேஸ்வரன் அக்கா  ','தர்மபாலன் சதுவாசகன் அண்ணா ','சுரேஷ்குமரன் ராம்சரண் அண்ணா ','சுசீந்திரன் அருள்ராஜ் ஹர்ஷியன் அண்ணா ','புராதனி நித்தியானந்தம் அக்கா  ','ஆனந்தி ஸ்ரீதரன் அக்கா ','ஸ்ரீனிவாசன் அபிலாஷ் அண்ணா','மனோகரன் அபிவருண் அண்ணா','ஜோன் தேவதாஸ் ஜொஷியா அண்ணா']
  b = ['சுதர்சன் குற்றாலன் ','பார்த்திபன் லக்ஷ்மன்','நித்தியகுமார் சயனுதன்','பிரபாகரன் பேருஷன் ','தவராசா ராகுல்','சிவகுமார் துவாரகா','சிவகணேசன் மயுரேஷ்','சுரேஷ் லதூஷன்','ராசேந்திரம் ஸபரீசன்','விஜயகுமார் கிருஷிகேசன்','திருச்செல்வம் அபிகீர்த்தன்','தக்ஷன்னா தெய்வேந்திரன்','நேசராஜ் டனுஷ்டன்','நிலாதரன் ரேணுராஜ்','தமிழ்செல்வம் தனேஷ்','சிங்கராஜா ரபிலக்ஷன்','சிவக்குமார் கிர்ஷிகன்','மோனிக்கா நரேந்திரநாத்','கலைஞானசுந்தரம் நிகிதன்']
  if (c<19):
    c=c
  else:
    c=(c-15)

  for i in range(19):
      nameof24batch=b[i]
      d=i+c
      if (d<19):
          nameof23batch=a[d]
          print(f"{nameof24batch}:-{nameof23batch}")
      else:
          nameof23batch=a[(d-19)]
          print(f"{nameof24batch}:-{nameof23batch}")

  nameof24batch='ரக்சனா லோகேஸ்பரன்'
  e=c
  if (c<19):
    nameof23batch=a[e]
    print(f"{nameof24batch}:-{nameof23batch}")
  else:
    nameof23batch=a[(e-5)]
    print(f"{nameof24batch}:-{nameof23batch}")

  nameof24batch='டிலக்சினி விஜயேந்திரராசா'
  f=c+1
  if (f<19):
    nameof23batch=a[f]
    print(f"{nameof24batch}:-{nameof23batch}")
  else:
    nameof23batch=a[f-2]
    print(f"{nameof24batch}:-{nameof23batch}")

  nameof24batch='ரக்க்ஷிகா லோகேஸ்பரன்'
  g=(c+3)
  if (g<19):
    nameof23batch=a[g]
    print(f"{nameof24batch}:-{nameof23batch}")
  else:
    g=g-4
    nameof23batch=a[g]
    print(f"{nameof24batch}:-{nameof23batch}")

  nameof24batch='யோகவி கயேந்திரன்'
  h=(c+2)
  if (h<19):
    nameof23batch=a[h]
    print(f"{nameof24batch}:-{nameof23batch}")
  else:
    nameof23batch=a[(h-3)]
    print(f"{nameof24batch}:-{nameof23batch}")

  print()
  