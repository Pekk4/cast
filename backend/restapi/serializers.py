from rest_framework import serializers

from .models import Employees
from .models import Employee_tech_skills
from .models import Techs


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Techs
        fields = ('tech_name')

class TechSkillSerializer(serializers.ModelSerializer):
    tech_name = serializers.StringRelatedField(source='tech.tech_name')
    class Meta:
        model = Employee_tech_skills
        fields = ('skill_level', 'tech', 'tech_name')

class ConsultantSerializer(serializers.ModelSerializer):
    skills = TechSkillSerializer(many=True)
    class Meta:
        model = Employees
        # fields = ('first_name', 'last_name', 'email', 'skills')
        fields = ('__all__')
        depth = 2
    
    def update(self, instance, validated_data):
        '''
            TBD: change changes to all employee-fields. 
            Con
        '''
           
        
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.location_country = validated_data.get('location_country', instance.location_country)
        instance.location_city = validated_data.get('location_city', instance.location_city)
        instance.worktime_allocation = validated_data.get('worktime_allocation', instance.worktime_allocation)
        instance.allocation_until = validated_data.get('allocation_until', instance.allocation_until)
        instance.wants_to_do = validated_data.get('wants_to_do', instance.wants_to_do)
        instance.wants_not_to_do = validated_data.get('wants_not_to_do', instance.wants_not_to_do)
        instance.save()

        if 'skills' in validated_data:

            updated_skill_list = validated_data.pop('skills')
            consultant_skills = list((instance.skills).all())


            for updated_skill in updated_skill_list:
                updated = False
                for skill in consultant_skills:
                    if updated_skill['tech']== skill.tech:
                        skill.skill_level = updated_skill['skill_level']
                        skill.save()
                        updated = True
                if not updated:
                    Employee_tech_skills.objects.create(employee=instance, tech=updated_skill['tech'], skill_level=updated_skill['skill_level'])
        return instance
    
