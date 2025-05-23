# -*- coding: utf-8 -*-
"""CF_Prak AI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MCGkYPpEOUtY0TUWkGjCSNMGnXSqRpe3
"""

gejala_user = {
    "demam": 0.7,
    "batuk": 0.8,
    "sakit_tenggorokan": 0.6,
    "pilek": 0.7,
    "pusing": 0.8,
    "hidung_tersumbat": 0.6,
    "mengigil": 0.7,
    "kelelahan": 0.8
}
#jika nilai demam diubah dari 0.7 -> 0.2 maka tidak akan pasti yakni bersifat netral 0.5
pengetahuan = {
    "flu": {
        "demam": 0.7,
        "batuk": 0.8,
        "sakit_tenggorokan": 0.6,
        "pilek": 0.7,
        "pusing": 0.8,
        "hidung_tersumbat": 0.6,
        "mengigil": 0.7,
        "kelelahan": 0.8
    }
}
#kesimpulannya jika 5 tambahan gejala dengan nilai > 0.5 akan menghasilkan jawaban pasti --> 1
def hitung_cf(gejala_user, pengetahuan_pakar):
  cf_total = 0
  first = True
  for gejala, cf_user in gejala_user.items():
    if gejala in pengetahuan_pakar:
      cf_pakar = pengetahuan_pakar[gejala]
      cf = cf_user * cf_pakar
      if first:
        cf_total = cf
        first = False
      else:
        cf_total = cf_total + cf * (1 - cf_total)
  return cf_total

cf_flu = hitung_cf(gejala_user, pengetahuan["flu"])
print(f"cf diagnosis flu: {cf_flu:.2f}")

gejala_user = {
    "nyeri_sendi": 0.8,
    "bengkak_sendi": 0.7,
    "kaku_sendi_pagi": 0.9,
    "demam_ringan": 0.3,
    "nyeri_otot": 0.4,
    "lemas": 0.7,
    "pegal": 0.6,
    "kesemutan": 0.5,
    "gatal": 0.7
}
#rentang 0.0 --> 1.0 sangat berpengaruh menentukan hasil diagnosa
pengetahuan = {
    "rheumatoid_arthritis": {
        "nyeri_sendi": 0.9,
        "bengkak_sendi": 0.8,
        "kaku_sendi_pagi": 0.9,
        "demam_ringan": 0.4,
        "lemas": 0.7,
        "pegal": 0.6,
        "gatal": 0.7
    },
    "osteorarthritis": {
        "nyeri_sendi": 0.8,
        "bengkak_sendi": 0.6,
        "kaku_sendi_pagi": 0.5,
        "nyeri_otot": 0.4,
        "kesemutan": 0.5,
    }
}

def hitung_cf(gejala_user, pengetahuan_pakar):
  cf_total = 0
  first = True
  for gejala, cf_user in gejala_user.items():
    if gejala in pengetahuan_pakar:
      cf_pakar = pengetahuan_pakar[gejala]
      cf = cf_user * cf_pakar
      if first:
        cf_total = cf
        first = False
      else:
        cf_total = cf_total + cf * (1 - cf_total)
  return cf_total

  #mendiagnosa dua penyakit berdasarkan gejala yang sama
for penyakit in pengetahuan:
   cf_result = hitung_cf(gejala_user, pengetahuan[penyakit])
   print(f"CF diagnosis {penyakit}: {cf_result:.2f}")

#example 4: diabetes diagnosis with weighted symptoms
gejala_user = {
    "sering_haus": 0.8,
    "sering_buang_air_kecil": 0.9,
    "penururnan_berat_badan": 0.6,
    "luka_lambat_sembuh": 0.7,
    "penglihatan_kabur": 0.5,
    "mudah_lemas": 0.7,
    "kesemutan": 0.4,
    "sakit_kepala": 0.6,
    "mual": 0.7,
    "infeksi": 0.5
}
# rentang nilai 0.0 --> 1.0 sangat berpengaruh dalam menentukan hasil diagnosa pasti dan tidak pastinya.
pengetahuan = {
    "diabetes_tipe1": {
        "sering_haus": 0.8,
        "sering_buang_air_kecil": 0.9,
        "penurunan_berat_badan": 0.6,
        "luka_lambat_sembuh": 0.7,
        "mudah_lemas": 0.7,
        "kesemutan": 0.4,
        "sakit_kepala": 0.6,
        "mual": 0.7,
        "infeksi": 0.5
    },
    "diabetes_tipe2": {
        "sering_haus": 0.8,
        "sering_buang_air_kecil": 0.9,
        "penurunan_berat_badan": 0.6,
        "luka_lambat_sembuh": 0.7,
        "penglihatan_kabur": 0.5,
        "kesemutan": 0.4,
        "sakit_kepala": 0.6,
        "mual": 0.7,
        "infeksi": 0.5
    }
}

#bobot kepentingan gejala (1-5)
bobot_gejala = {
    "sering_haus": 4,
    "sering_buang_air_kecil": 4,
    "penururnan_berat_badan": 3,
    "luka_lambat_sembuh": 5,
    "penglihatan_kabur": 2,
    "mudah_lemas": 3,
    "kesemutan": 4,
    "sakit_kepala": 6,
    "mual": 7,
    "infeksi": 5

}

def hitung_cf_weighted(gejala_user, pengetahuan_pakar, bobot):
  cf_total = 0
  first = True
  total_bobot = 0

  for gejala, cf_user in gejala_user.items():
    if gejala in pengetahuan_pakar and gejala in bobot:
      cf_pakar = pengetahuan_pakar[gejala]
      gejala_weight = bobot[gejala] / 5 #normalisasi bobot (1-5) --> (0.2-1.0)
      cf = cf_user * cf_pakar * gejala_weight
      if first:
        cf_total = cf
        first = False
      else:
        cf_total = cf_total + cf * (1 - cf_total)

      total_bobot += gejala_weight

  #normalisasi hasil berdasarkan total bobot
  if total_bobot > 0:
    cf_total = cf_total / total_bobot * len([g for g in gejala_user if g in pengetahuan_pakar])

  return cf_total

  #mendiagnosa dua penyakit berdasarkan gejala yang sama
for penyakit in pengetahuan:
   cf_result = hitung_cf_weighted(gejala_user, pengetahuan[penyakit], bobot_gejala)
   print(f"CF diagnosis {penyakit}: {cf_result:.2f}")